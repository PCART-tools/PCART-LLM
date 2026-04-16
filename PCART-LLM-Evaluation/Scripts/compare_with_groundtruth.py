#!/usr/bin/env python3
"""Generate a semantic-split PCBench ground-truth comparison report.

Usage:
  python Test/compare_with_groundtruth.py <result_root> <manifest_json> <report.md>
  python Test/compare_with_groundtruth.py <result_root> <manifest_json> <report.md> --gt-root <groundtruth_root>

The manifest should contain files.delete_or_rename. Files listed there are
treated as semantic-related samples, while the remaining prediction JSON files
are treated as semantic-unrelated samples.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_GT_ROOT = Path(
    "/Users/ganymede/Downloads/Workspace/RE/Tag/"
    "PCBench-LLM-Distilled-NaN-groundTruth/"
    "PCBench-LLM-Distilled-NaN-groundTruth-DictOnly"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "按语义命中清单切分 PCBench 结果，并分别与 DictOnly ground truth "
            "比对，输出语义相关、语义不相关和合并后的正确率报告。"
        )
    )
    parser.add_argument(
        "result_root",
        help="待比对的结果目录，可以是实验根目录，也可以直接是 Benchmark 目录",
    )
    parser.add_argument(
        "manifest",
        help="语义切分依据 JSON，例如 json_contains_delete_or_rename_report.json",
    )
    parser.add_argument(
        "output",
        help="Markdown 报告输出路径，例如 reports/semantic_split_report.md",
    )
    parser.add_argument(
        "--gt-root",
        default=str(DEFAULT_GT_ROOT),
        help="DictOnly ground truth 目录；省略时使用脚本内置默认路径",
    )
    return parser.parse_args()


def resolve_benchmark_dir(path_str: str) -> Path:
    base = Path(path_str).expanduser().resolve()
    candidates = [
        base,
        base / "Benchmark",
        base / "PCBench-LLM-Distilled-NaN" / "Benchmark",
    ]
    for candidate in candidates:
        if candidate.is_dir() and candidate.name == "Benchmark":
            return candidate
    raise FileNotFoundError(f"未找到 Benchmark 目录: {base}")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_prediction(payload: Any) -> Any:
    if not isinstance(payload, dict):
        return payload

    extracted = []
    for item in payload.get("repairLst", []):
        if isinstance(item, dict) and "repairDict" in item:
            extracted.append(item["repairDict"])
        else:
            extracted.append(item)
    return extracted


def build_index(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(root.rglob("*.json"))
    }


def strip_path_prefix(path_parts: tuple[str, ...], prefix_parts: tuple[str, ...]) -> str | None:
    if not prefix_parts:
        return None

    max_start = len(path_parts) - len(prefix_parts)
    for start in range(max_start + 1):
        end = start + len(prefix_parts)
        if path_parts[start:end] == prefix_parts:
            return Path(*path_parts[end:]).as_posix()
    return None


def manifest_hit_set(manifest_path: Path, gt_root: Path) -> set[str]:
    payload = load_json(manifest_path)
    entries = payload["files"]["delete_or_rename"]
    source_directory = payload.get("source_directory")
    prefix_parts = (
        Path(source_directory).parts
        if source_directory
        else gt_root.expanduser().resolve().parts
    )
    hit_set = set()

    for entry in entries:
        parts = Path(entry).parts
        rel_path = strip_path_prefix(parts, prefix_parts)
        if rel_path is None:
            raise ValueError(
                "manifest 条目未匹配 ground truth 前缀 "
                f"{Path(*prefix_parts).as_posix()}: {entry}"
            )
        hit_set.add(rel_path)

    return hit_set


def mismatch_reason(pred: Any, gt: Any) -> str:
    if type(pred) is not type(gt):
        return f"type mismatch: pred={type(pred).__name__}, gt={type(gt).__name__}"

    if isinstance(pred, list) and isinstance(gt, list):
        if len(pred) != len(gt):
            return f"list length mismatch: pred={len(pred)}, gt={len(gt)}"
        for idx, (pred_item, gt_item) in enumerate(zip(pred, gt)):
            if pred_item == gt_item:
                continue
            if isinstance(pred_item, dict) and isinstance(gt_item, dict):
                pred_keys = set(pred_item)
                gt_keys = set(gt_item)
                if pred_keys != gt_keys:
                    return (
                        f"item {idx} keys mismatch: "
                        f"pred_only={sorted(pred_keys - gt_keys)[:3]}, "
                        f"gt_only={sorted(gt_keys - pred_keys)[:3]}"
                    )
                for key in sorted(pred_keys):
                    if pred_item[key] != gt_item[key]:
                        pred_value = repr(pred_item[key])[:80]
                        gt_value = repr(gt_item[key])[:80]
                        return (
                            f"item {idx} field {key} mismatch: "
                            f"pred={pred_value}, gt={gt_value}"
                        )
            return f"item {idx} mismatch"
        return "list content mismatch"

    return "value mismatch"


def compute_stats(
    rel_paths: list[str],
    pred_files: dict[str, Path],
    gt_files: dict[str, Path],
) -> dict[str, Any]:
    correct = 0
    errors: list[dict[str, str]] = []

    for rel_path in rel_paths:
        pred_path = pred_files.get(rel_path)
        gt_path = gt_files.get(rel_path)

        if pred_path is None:
            errors.append(
                {
                    "path": rel_path,
                    "type": "missing_pred",
                    "detail": "result file missing",
                }
            )
            continue

        if gt_path is None:
            errors.append(
                {
                    "path": rel_path,
                    "type": "missing_gt",
                    "detail": "ground truth missing",
                }
            )
            continue

        pred_payload = extract_prediction(load_json(pred_path))
        gt_payload = load_json(gt_path)
        if pred_payload == gt_payload:
            correct += 1
        else:
            errors.append(
                {
                    "path": rel_path,
                    "type": "mismatch",
                    "detail": mismatch_reason(pred_payload, gt_payload),
                }
            )

    total = len(rel_paths)
    wrong = len(errors)
    accuracy = (correct / total * 100.0) if total else 0.0
    return {
        "total": total,
        "correct": correct,
        "wrong": wrong,
        "accuracy": accuracy,
        "errors": errors,
    }


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def summary_table_row(label: str, stats: dict[str, Any]) -> str:
    return (
        f"| {label} | {stats['total']} | {stats['correct']} | "
        f"{stats['wrong']} | {stats['accuracy']:.2f}% |"
    )


def stats_block(stats: dict[str, Any]) -> list[str]:
    return [
        "| 指标 | 数值 |",
        "| --- | ---: |",
        f"| 样例数 | {stats['total']} |",
        f"| 正确 | {stats['correct']} |",
        f"| 错误 | {stats['wrong']} |",
        f"| 正确率 | {stats['accuracy']:.2f}% |",
    ]


def errors_block(errors: list[dict[str, str]]) -> list[str]:
    lines = [
        "| 序号 | 样例路径 | 错误类型 | 差异说明 |",
        "| --- | --- | --- | --- |",
    ]
    if not errors:
        lines.append("| 1 | 无 | 无 | 本部分没有错误样例 |")
        return lines

    for idx, item in enumerate(errors, start=1):
        lines.append(
            f"| {idx} | `{escape_cell(item['path'])}` | {item['type']} | "
            f"{escape_cell(item['detail'])} |"
        )
    return lines


def build_markdown(
    manifest_path: Path,
    pred_root: Path,
    gt_root: Path,
    related_stats: dict[str, Any],
    unrelated_stats: dict[str, Any],
    overall_stats: dict[str, Any],
) -> str:
    lines = [
        "# PCBench-LLM-Distilled-NaN 语义切分对比报告",
        "",
        "## 说明",
        "",
        f"- 切分依据：`{manifest_path}`",
        "- 命中 `files.delete_or_rename` 的样例记为“语义相关”",
        "- 未命中的样例记为“语义不相关”",
        f"- 对比结果目录：`{pred_root}`",
        f"- 对比 ground truth：`{gt_root}`",
        "- 判定规则：结果 JSON 中的 `repairLst[].repairDict` 与对应 ground truth JSON 完全一致则记为“正确”，否则记为“错误”",
        "",
        "## 总体统计",
        "",
        "| 部分 | 样例数 | 正确 | 错误 | 正确率 |",
        "| --- | ---: | ---: | ---: | ---: |",
        summary_table_row("语义相关", related_stats),
        summary_table_row("语义不相关", unrelated_stats),
        summary_table_row("合并后", overall_stats),
        "",
        "## 语义相关",
        "",
    ]
    lines.extend(stats_block(related_stats))
    lines.extend(["", "### 错误样例", ""])
    lines.extend(errors_block(related_stats["errors"]))
    lines.extend(["", "## 语义不相关", ""])
    lines.extend(stats_block(unrelated_stats))
    lines.extend(["", "### 错误样例", ""])
    lines.extend(errors_block(unrelated_stats["errors"]))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    pred_root = resolve_benchmark_dir(args.result_root)
    manifest_path = Path(args.manifest).expanduser().resolve()
    gt_root = Path(args.gt_root).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not manifest_path.is_file():
        raise FileNotFoundError(f"语义切分依据文件不存在: {manifest_path}")
    if not gt_root.is_dir():
        raise FileNotFoundError(f"ground truth 目录不存在: {gt_root}")

    pred_files = build_index(pred_root)
    gt_files = build_index(gt_root)

    all_rel_paths = sorted(pred_files)
    hit_set = manifest_hit_set(manifest_path, gt_root)
    related_paths = sorted(rel_path for rel_path in all_rel_paths if rel_path in hit_set)
    unrelated_paths = sorted(rel_path for rel_path in all_rel_paths if rel_path not in hit_set)

    related_stats = compute_stats(related_paths, pred_files, gt_files)
    unrelated_stats = compute_stats(unrelated_paths, pred_files, gt_files)

    overall_correct = related_stats["correct"] + unrelated_stats["correct"]
    overall_wrong = related_stats["wrong"] + unrelated_stats["wrong"]
    overall_total = len(all_rel_paths)
    overall_stats = {
        "total": overall_total,
        "correct": overall_correct,
        "wrong": overall_wrong,
        "accuracy": (overall_correct / overall_total * 100.0) if overall_total else 0.0,
    }

    markdown = build_markdown(
        manifest_path=manifest_path,
        pred_root=pred_root,
        gt_root=gt_root,
        related_stats=related_stats,
        unrelated_stats=unrelated_stats,
        overall_stats=overall_stats,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")

    print("=== 语义切分期待结果比对 ===")
    print(f"manifest={manifest_path}")
    print(f"pred_root={pred_root}")
    print(f"gt_root={gt_root}")
    print(f"output={output_path}")
    print(f"semantic_related={related_stats['total']}")
    print(f"semantic_related_correct={related_stats['correct']}")
    print(f"semantic_related_wrong={related_stats['wrong']}")
    print(f"semantic_related_accuracy={related_stats['accuracy']:.2f}%")
    print(f"semantic_unrelated={unrelated_stats['total']}")
    print(f"semantic_unrelated_correct={unrelated_stats['correct']}")
    print(f"semantic_unrelated_wrong={unrelated_stats['wrong']}")
    print(f"semantic_unrelated_accuracy={unrelated_stats['accuracy']:.2f}%")
    print(f"overall_total={overall_stats['total']}")
    print(f"overall_correct={overall_stats['correct']}")
    print(f"overall_wrong={overall_stats['wrong']}")
    print(f"overall_accuracy={overall_stats['accuracy']:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
