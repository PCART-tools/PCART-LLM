#!/usr/bin/env python3
"""
为 PCBench-LLM-Distilled/Benchmark/ 下的每个样本生成 JSON 配置文件。
基于 PCBench/generateJson.py 修改。
"""

from __future__ import annotations

import os
import json
from pathlib import Path

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 配置目录
BENCHMARK_DIR = PROJECT_ROOT / "Benchmark"


def get_subdirs(path: Path) -> list[Path]:
    """获取目录下的所有子目录"""
    if not path.exists():
        return []
    return sorted([d for d in path.iterdir() if d.is_dir()])


def main():
    print("=" * 50)
    print("PCBench-LLM JSON 配置文件生成器")
    print("=" * 50)

    if not BENCHMARK_DIR.exists():
        print(f"错误: 目录 '{BENCHMARK_DIR}' 不存在")
        return

    # 交互式输入环境目录
    print("\n请输入 conda 环境所在的目录路径")
    print("(例如: /path/to/envs 或 ~/miniconda3/envs)")
    print("-" * 50)
    envs_path = input("环境目录: ").strip()

    if not envs_path:
        print("错误: 路径不能为空")
        return

    # 展开用户目录和转换为绝对路径
    envs_path = os.path.abspath(os.path.expanduser(envs_path))

    # 确认路径
    print(f"\n环境目录将设置为: {envs_path}")
    if input("确认? (y/n): ").strip().lower() != 'y':
        print("已取消")
        return

    print("\n" + "=" * 70)
    print("Generating JSON files for PCBench-LLM...")
    print("=" * 70)

    # 遍历每个库
    lib_dirs = get_subdirs(BENCHMARK_DIR)
    total_json_count = 0

    for lib_path in lib_dirs:
        lib_name = lib_path.name
        json_count = 0

        # 遍历库下的每个 API
        api_dirs = get_subdirs(lib_path)

        for api_path in api_dirs:
            api_dir_name = api_path.name  # e.g., aiohttp.TCPConnector@2.3.10-3.0.0#L

            # 移除兼容性标签后缀 (#C, #H, #L)
            if api_dir_name.endswith(('#C', '#H', '#L')):
                api_dir_name_clean = api_dir_name[:-2]
            else:
                api_dir_name_clean = api_dir_name

            # 解析 API 名称和版本
            # 格式: libName.apiName@currentVersion-targetVersion
            if "@" in api_dir_name_clean:
                api_full_name, version_range = api_dir_name_clean.rsplit("@", 1)
                api_name = api_full_name.split(".")[-1]
                if "-" in version_range:
                    current_version, target_version = version_range.split("-", 1)
                else:
                    current_version = target_version = version_range
            else:
                api_name = api_dir_name_clean.split(".")[-1]
                current_version = target_version = "unknown"

            # 遍历每个示例
            example_dirs = get_subdirs(api_path)

            for example_path in example_dirs:
                example_name = example_path.name  # e.g., aiohttp.TCPConnector#4NN
                label = example_name[-2:]  # NN or YY

                # 构建 JSON 文件路径
                json_filename = f"{api_name}{label}.json"
                json_path = example_path / json_filename

                # 构建配置 - 使用用户输入的环境目录
                config = {
                    "projPath": str(example_path),
                    "runCommand": f"python {api_name}{label}.py",
                    "runFilePath": "",
                    "libName": lib_name,
                    "currentVersion": current_version,
                    "targetVersion": target_version,
                    "currentEnv": f"{envs_path}/{lib_name}{current_version}",
                    "targetEnv": f"{envs_path}/{lib_name}{target_version}",
                }

                # 写入 JSON 文件
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(config, f, indent=4, ensure_ascii=False)

                json_count += 1

        if json_count > 0:
            print(f"{lib_name}: {json_count} JSON files generated")
            total_json_count += json_count

    print("=" * 70)
    print(f"Done! Total: {total_json_count} JSON files generated")
    print(f"环境路径前缀: {envs_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
