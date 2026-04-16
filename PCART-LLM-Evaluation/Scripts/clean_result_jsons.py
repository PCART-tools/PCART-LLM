#!/usr/bin/env python3
"""Clean result JSON files by a manifest file.

Usage:
  python Test/clean_result_jsons.py <target_root> <manifest_json>
  python Test/clean_result_jsons.py <target_root> <manifest_json> --apply

The script keeps only the JSON files listed in the manifest, deletes other
JSON files when --apply is passed, and always preserves TXT files.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "按 manifest 清理结果目录中的 JSON 文件。默认只预览，不删除；"
            "添加 --apply 后才会实际删除多余 JSON。"
        )
    )
    parser.add_argument(
        "target_root",
        type=Path,
        help="要清理的结果目录，例如某次实验输出目录或其中的 Benchmark 目录",
    )
    parser.add_argument(
        "manifest",
        type=Path,
        help="作为清理依据的 manifest JSON，例如 log_nan_valid_samples_and_target_jsons.json",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="实际删除多余 JSON 文件；不加该参数时只进行 dry-run 预览",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="即使 manifest 中列出的 JSON 在目标目录中缺失，也继续删除多余 JSON",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=10,
        help="输出多余文件或缺失文件样例的最大数量，默认 10",
    )
    return parser.parse_args()


def load_manifest(manifest_path: Path) -> tuple[dict, list[tuple[str, tuple[str, ...]]]]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    relative_root = data["relative_root"]
    keep_suffixes: list[tuple[str, tuple[str, ...]]] = []

    for entry in data["entries"]:
        sample_dir = Path(entry["sample_dir"])
        for target_json in entry["target_jsons"]:
            suffix = Path(relative_root) / sample_dir / target_json
            keep_suffixes.append((suffix.as_posix(), suffix.parts))

    return data, keep_suffixes


def ends_with_parts(path_parts: tuple[str, ...], suffix_parts: tuple[str, ...]) -> bool:
    if len(path_parts) < len(suffix_parts):
        return False
    return path_parts[-len(suffix_parts) :] == suffix_parts


def collect_actual_jsons(target_root: Path) -> list[tuple[Path, tuple[str, ...], str]]:
    actual: list[tuple[Path, tuple[str, ...], str]] = []
    for path in sorted(target_root.rglob("*.json")):
        relative = path.relative_to(target_root)
        actual.append((path, relative.parts, relative.as_posix()))
    return actual


def print_sample(title: str, values: list[str], sample_size: int) -> None:
    if not values:
        return
    print()
    print(f"{title}:")
    for value in values[:sample_size]:
        print(value)


def main() -> int:
    args = parse_args()
    target_root = args.target_root.expanduser().resolve()
    manifest_path = args.manifest.expanduser().resolve()

    if not target_root.is_dir():
        print(f"目标目录不存在: {target_root}", file=sys.stderr)
        return 1
    if not manifest_path.is_file():
        print(f"manifest 文件不存在: {manifest_path}", file=sys.stderr)
        return 1

    _, keep_suffixes = load_manifest(manifest_path)
    keep_lookup = {suffix_parts: suffix_str for suffix_str, suffix_parts in keep_suffixes}
    matched_suffixes: set[tuple[str, ...]] = set()
    extra_files: list[Path] = []
    extra_rel_paths: list[str] = []

    for path, rel_parts, rel_str in collect_actual_jsons(target_root):
        matched = False
        for suffix_parts in keep_lookup:
            if ends_with_parts(rel_parts, suffix_parts):
                matched = True
                matched_suffixes.add(suffix_parts)
                break
        if not matched:
            extra_files.append(path)
            extra_rel_paths.append(rel_str)

    missing_rel_paths = [
        keep_lookup[suffix_parts]
        for suffix_parts in keep_lookup
        if suffix_parts not in matched_suffixes
    ]
    txt_count = sum(1 for _ in target_root.rglob("*.txt"))

    print("=== 结果 JSON 清理 ===")
    print(f"target_root={target_root}")
    print(f"manifest={manifest_path}")
    print(f"mode={'apply' if args.apply else 'dry-run'}")
    print(f"keep_listed={len(keep_lookup)}")
    print(f"actual_json={len(extra_files) + len(matched_suffixes)}")
    print(f"extra_json={len(extra_files)}")
    print(f"missing_json={len(missing_rel_paths)}")
    print(f"txt_count={txt_count}")

    print_sample("EXTRA sample", extra_rel_paths, args.sample_size)
    print_sample("MISSING sample", missing_rel_paths, args.sample_size)

    if missing_rel_paths and not args.allow_missing:
        print()
        print("检测到 manifest 中列出的 JSON 缺失，已停止删除。")
        print("确认仍需删除多余 JSON 时，请添加 --allow-missing --apply。")
        return 2

    deleted = 0
    if args.apply:
        for path in extra_files:
            path.unlink()
        deleted = len(extra_files)
    else:
        print()
        print("当前为 dry-run，仅展示将被删除的 JSON，未修改任何文件。")

    remaining_json = sum(1 for _ in target_root.rglob("*.json"))
    print(f"deleted_json={deleted}")
    print(f"remaining_json={remaining_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
