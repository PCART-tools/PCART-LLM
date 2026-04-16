#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
南航云盘环境下载脚本
功能：选择文件夹，下载文件并解压到指定目录
"""

import requests
import os
import zipfile
import tarfile
from pathlib import Path
from typing import List, Dict, Tuple
import time
import re


class DownloadStats:
    """下载统计"""
    def __init__(self):
        self.success_count = 0
        self.fail_count = 0
        self.skip_count = 0
        self.total_size = 0
        self.start_time = None
        self.end_time = None
        self.failed_files: List[Dict] = []  # 记录失败的文件详情

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def add_success(self, size: int = 0):
        self.success_count += 1
        self.total_size += size

    def add_fail(self, filename: str = "", error: str = ""):
        self.fail_count += 1
        if filename:
            self.failed_files.append({"filename": filename, "error": error})

    def add_skip(self, filename: str = "", reason: str = ""):
        self.skip_count += 1
        if filename:
            self.failed_files.append({"filename": filename, "error": f"跳过: {reason}"})

    def get_duration(self) -> float:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0

    def format_duration(self) -> str:
        duration = self.get_duration()
        if duration < 60:
            return f"{duration:.1f}秒"
        elif duration < 3600:
            return f"{duration/60:.1f}分钟"
        else:
            return f"{duration/3600:.1f}小时"


class NuaaPanDownloader:
    def __init__(self, share_url: str):
        self.share_url = share_url
        self.share_token = self._extract_share_token()
        self.base_url = "https://pan.nuaa.edu.cn"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': self.share_url,
            'X-Requested-With': 'XMLHttpRequest'
        })
        # 初始化session，获取必要的cookie
        self._init_session()
        # 统计
        self.stats = DownloadStats()

    def _extract_share_token(self) -> str:
        match = re.search(r'/share/([^/?]+)', self.share_url)
        if match:
            return match.group(1)
        raise ValueError("无法从URL中提取share_token")

    def _init_session(self):
        """访问分享页面初始化session和cookie"""
        self.session.get(self.share_url)

    def _get_main_folder_id(self) -> int:
        """从API获取主文件夹ID"""
        url = f"{self.base_url}/apps/files/get_info"
        params = {
            'scenario': 'share',
            'item_typed_id': f'folder_{self.share_token}',
            '_': int(time.time() * 1000)
        }
        try:
            response = self.session.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and 'id' in data:
                    return data['id']
        except:
            pass
        return 501007473659  # 默认值

    def get_folders(self) -> List[Dict]:
        """获取所有文件夹列表"""
        main_folder_id = self._get_main_folder_id()
        url = f"{self.base_url}/apps/files/file_list/{main_folder_id}"
        params = {
            'page_number': 1,
            'scenario': 'share',
            'sort_by': 'name',
            'sort_direction': 'asc',
            'page_size': 100,
            'share_token': self.share_token,
            '_': int(time.time() * 1000)
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get('success'):
                folders = []
                for item in data.get('children', []):
                    if item.get('type') == 'folder':
                        folders.append({
                            'name': item.get('name'),
                            'id': item.get('id'),
                            'size': item.get('size', 0),
                            'item_count': item.get('item_count', 0)
                        })
                return folders
        except Exception as e:
            print(f"获取文件夹列表失败: {e}")
        return []

    def get_folder_files(self, folder_id: int) -> List[Dict]:
        """获取文件夹内所有文件"""
        all_files = []
        page_number = 1

        while True:
            url = f"{self.base_url}/apps/files/file_list/{folder_id}"
            params = {
                'page_number': page_number,
                'scenario': 'share',
                'sort_by': 'name',
                'sort_direction': 'asc',
                'page_size': 100,
                'share_token': self.share_token,
                '_': int(time.time() * 1000)
            }

            try:
                response = self.session.get(url, params=params)
                data = response.json()

                if data.get('success'):
                    files = [item for item in data.get('children', []) if item.get('type') == 'file']
                    all_files.extend(files)
                    if page_number >= data.get('page_count', 1):
                        break
                    page_number += 1
                else:
                    break
            except:
                break

        return all_files

    def get_download_url(self, file_id: int) -> str:
        """获取文件真实下载链接（通过302重定向）"""
        url = f"{self.base_url}/apps/files/download"
        params = {
            'file_id': file_id,
            'scenario': 'share',
            'unique_name': self.share_token  # 关键：使用unique_name而不是share_token
        }

        try:
            response = self.session.get(url, params=params, allow_redirects=False)
            if response.status_code == 302:
                return response.headers.get('Location', '')
        except Exception as e:
            print(f"  获取下载链接失败: {e}")
        return None

    def download_file(self, download_url: str, save_path: str, max_retries: int = 3) -> Tuple[bool, int, str]:
        """下载文件，返回 (成功与否, 文件大小, 错误信息)"""
        last_error = ""

        for attempt in range(1, max_retries + 1):
            try:
                if attempt > 1:
                    print(f"  重试 {attempt}/{max_retries}...")
                    time.sleep(1)  # 重试前等待1秒

                response = self.session.get(download_url, stream=True, timeout=30)
                response.raise_for_status()

                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0

                os.makedirs(os.path.dirname(save_path) or '.', exist_ok=True)

                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                percent = (downloaded / total_size) * 100
                                print(f"\r  进度: {percent:.1f}% ({self.format_size(downloaded)}/{self.format_size(total_size)})", end='', flush=True)
                print()

                if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
                    return True, os.path.getsize(save_path), ""

                last_error = "下载的文件为空"

            except requests.exceptions.Timeout:
                last_error = "连接超时"
                print(f"\n  连接超时")
            except requests.exceptions.ConnectionError as e:
                last_error = f"连接错误: {str(e)[:50]}"
                print(f"\n  连接错误")
            except requests.exceptions.HTTPError as e:
                last_error = f"HTTP错误: {e.response.status_code}"
                print(f"\n  HTTP错误: {e.response.status_code}")
            except Exception as e:
                last_error = str(e)[:100]
                print(f"\n  下载失败: {e}")

            # 清理失败的临时文件
            if os.path.exists(save_path):
                try:
                    os.remove(save_path)
                except:
                    pass

        print(f"  ✗ 重试{max_retries}次后仍然失败")
        return False, 0, last_error

    def extract_archive(self, archive_path: str, extract_to: str) -> bool:
        """解压压缩包"""
        try:
            os.makedirs(extract_to, exist_ok=True)

            if archive_path.endswith('.zip'):
                with zipfile.ZipFile(archive_path, 'r') as zf:
                    zf.extractall(extract_to)
            elif archive_path.endswith(('.tar.gz', '.tgz')):
                with tarfile.open(archive_path, 'r:gz') as tf:
                    tf.extractall(extract_to)
            elif archive_path.endswith('.tar'):
                with tarfile.open(archive_path, 'r') as tf:
                    tf.extractall(extract_to)
            else:
                print(f"不支持的压缩格式: {archive_path}")
                return False
            return True
        except Exception as e:
            print(f"解压失败: {e}")
            return False

    def format_size(self, size_bytes: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"

    def get_archive_basename(self, filename: str) -> str:
        """获取压缩包的基础名称（去掉扩展名）"""
        if filename.endswith('.tar.gz'):
            return filename[:-7]
        elif filename.endswith('.tgz'):
            return filename[:-4]
        elif filename.endswith('.tar'):
            return filename[:-4]
        elif filename.endswith('.zip'):
            return filename[:-4]
        return filename

    def download_folder(self, folder: Dict, install_path: str):
        """下载文件夹中的所有文件并解压"""
        folder_name = folder['name']
        folder_id = folder['id']

        print(f"\n处理文件夹: {folder_name}")

        files = self.get_folder_files(folder_id)
        if not files:
            print(f"  文件夹为空")
            return

        # 过滤压缩包
        archives = [f for f in files if f['name'].lower().endswith(('.zip', '.tar.gz', '.tgz', '.tar'))]
        if not archives:
            print(f"  没有找到压缩包")
            return

        print(f"  找到 {len(archives)} 个压缩包")

        temp_dir = os.path.join(install_path, '.temp')
        os.makedirs(temp_dir, exist_ok=True)

        for i, file_info in enumerate(archives, 1):
            file_name = file_info['name']
            file_id = file_info['id']

            print(f"\n  [{i}/{len(archives)}] {file_name} ({self.format_size(file_info.get('size', 0))})")

            # 获取下载链接
            download_url = self.get_download_url(file_id)
            if not download_url:
                print(f"  跳过: 无法获取下载链接")
                self.stats.add_skip(file_name, "无法获取下载链接")
                continue

            temp_file = os.path.join(temp_dir, file_name)

            # 下载（带重试）
            success, size, error = self.download_file(download_url, temp_file)
            if not success:
                self.stats.add_fail(file_name, error)
                continue

            # 解压到与压缩包同名的文件夹
            archive_basename = self.get_archive_basename(file_name)
            archive_extract_path = os.path.join(install_path, archive_basename)
            os.makedirs(archive_extract_path, exist_ok=True)
            print(f"  解压到: {archive_extract_path}")
            if self.extract_archive(temp_file, archive_extract_path):
                os.remove(temp_file)
                print(f"  ✓ 完成")
                self.stats.add_success(size)
            else:
                self.stats.add_fail(file_name, "解压失败")

        # 清理临时目录
        try:
            if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                os.rmdir(temp_dir)
        except:
            pass

    def download_single_files(self, folder: Dict, files: List[Dict], install_path: str):
        """下载指定的文件并解压"""
        folder_name = folder['name']

        print(f"\n处理文件夹: {folder_name}")
        print(f"  选中 {len(files)} 个文件")

        temp_dir = os.path.join(install_path, '.temp')
        os.makedirs(temp_dir, exist_ok=True)

        for i, file_info in enumerate(files, 1):
            file_name = file_info['name']
            file_id = file_info['id']

            print(f"\n  [{i}/{len(files)}] {file_name} ({self.format_size(file_info.get('size', 0))})")

            # 获取下载链接
            download_url = self.get_download_url(file_id)
            if not download_url:
                print(f"  跳过: 无法获取下载链接")
                self.stats.add_skip(file_name, "无法获取下载链接")
                continue

            temp_file = os.path.join(temp_dir, file_name)

            # 下载（带重试）
            success, size, error = self.download_file(download_url, temp_file)
            if not success:
                self.stats.add_fail(file_name, error)
                continue

            # 解压到与压缩包同名的文件夹
            archive_basename = self.get_archive_basename(file_name)
            archive_extract_path = os.path.join(install_path, archive_basename)
            os.makedirs(archive_extract_path, exist_ok=True)
            print(f"  解压到: {archive_extract_path}")
            if self.extract_archive(temp_file, archive_extract_path):
                os.remove(temp_file)
                print(f"  ✓ 完成")
                self.stats.add_success(size)
            else:
                self.stats.add_fail(file_name, "解压失败")

        # 清理临时目录
        try:
            if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                os.rmdir(temp_dir)
        except:
            pass

    def print_stats(self):
        """打印下载统计"""
        print("\n" + "=" * 50)
        print("下载统计")
        print("=" * 50)
        print(f"  成功: {self.stats.success_count}")
        print(f"  失败: {self.stats.fail_count}")
        print(f"  跳过: {self.stats.skip_count}")
        print(f"  总计: {self.stats.success_count + self.stats.fail_count + self.stats.skip_count}")
        print(f"  下载大小: {self.format_size(self.stats.total_size)}")
        print(f"  耗时: {self.stats.format_duration()}")

        # 输出失败详情，方便人工修正
        if self.stats.failed_files:
            print("\n" + "-" * 50)
            print("失败/跳过的文件详情:")
            print("-" * 50)
            for i, item in enumerate(self.stats.failed_files, 1):
                print(f"  {i}. {item['filename']}")
                print(f"     原因: {item['error']}")
            print("-" * 50)
            print("提示: 可以重新运行脚本，使用选择性下载模式单独下载这些文件")

        print("=" * 50)


def mode_batch_download(downloader: NuaaPanDownloader, folders: List[Dict]):
    """批量下载模式：选择多个文件夹下载所有内容"""
    print("\n" + "-" * 50)
    print("批量下载模式")
    print("-" * 50)

    # 选择文件夹
    choice = input("选择文件夹 (序号用逗号分隔，或输入 all): ").strip()

    if choice.lower() == 'all':
        selected = folders
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(',')]
            selected = [folders[i] for i in indices if 0 <= i < len(folders)]
        except:
            print("输入格式错误")
            return

    if not selected:
        print("未选择文件夹")
        return

    # 输入安装路径
    install_path = input("输入安装路径: ").strip()
    if not install_path:
        print("路径不能为空")
        return

    install_path = os.path.abspath(os.path.expanduser(install_path))

    # 确认
    print(f"\n将下载 {len(selected)} 个文件夹到: {install_path}")
    if input("确认? (y/n): ").strip().lower() != 'y':
        return

    # 下载
    downloader.stats = DownloadStats()
    downloader.stats.start()

    for folder in selected:
        downloader.download_folder(folder, install_path)

    downloader.stats.stop()
    downloader.print_stats()


def mode_selective_download(downloader: NuaaPanDownloader, folders: List[Dict]):
    """选择性下载模式：进入文件夹选择特定文件下载"""
    print("\n" + "-" * 50)
    print("选择性下载模式")
    print("-" * 50)

    # 输入安装路径
    install_path = input("输入安装路径: ").strip()
    if not install_path:
        print("路径不能为空")
        return

    install_path = os.path.abspath(os.path.expanduser(install_path))

    # 初始化统计
    downloader.stats = DownloadStats()
    downloader.stats.start()

    def show_folders():
        """显示文件夹列表"""
        print("\n可用文件夹:")
        for i, f in enumerate(folders, 1):
            print(f"  {i}. {f['name']} ({downloader.format_size(f['size'])}, {f['item_count']}个文件)")

    def show_files(archives: List[Dict]):
        """显示文件列表"""
        print(f"\n可用文件 ({len(archives)} 个):")
        for i, f in enumerate(archives, 1):
            print(f"  {i:2d}. {f['name']} ({downloader.format_size(f.get('size', 0))})")

    current_folder = None
    archives = []

    # 主循环
    while True:
        if current_folder is None:
            # 显示文件夹列表
            show_folders()
            print("\n" + "=" * 50)
            print("操作: 输入文件夹序号进入, /q 退出")
            print("=" * 50)

            choice = input("\n> ").strip()

            if choice.lower() in ['/q', 'q', 'exit', 'quit']:
                break

            try:
                folder_idx = int(choice) - 1
                if 0 <= folder_idx < len(folders):
                    current_folder = folders[folder_idx]
                    print(f"\n进入文件夹: {current_folder['name']}")
                    print("获取文件列表...")
                    files = downloader.get_folder_files(current_folder['id'])
                    archives = [f for f in files if f['name'].lower().endswith(('.zip', '.tar.gz', '.tgz', '.tar'))]
                    if not archives:
                        print("没有找到压缩包")
                        current_folder = None
                        continue
                else:
                    print("无效序号")
            except ValueError:
                print("无效输入")

        else:
            # 在文件夹内，显示文件列表
            show_files(archives)
            print("\n" + "=" * 50)
            print("操作: 序号下载 (如: 1 或 1,2,3), /a 下载全部, /b 返回文件夹列表, /q 退出")
            print("=" * 50)

            choice = input("\n> ").strip()

            if not choice:
                continue

            # 退出
            if choice.lower() in ['/q', 'q', 'exit', 'quit']:
                break

            # 返回文件夹列表
            if choice.lower() == '/b':
                current_folder = None
                archives = []
                continue

            # 下载全部
            if choice.lower() == '/a':
                print(f"\n将下载全部 {len(archives)} 个文件")
                if input("确认? (y/n): ").strip().lower() == 'y':
                    downloader.download_single_files(current_folder, archives, install_path)
                continue

            # 解析序号下载
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                selected_files = []
                invalid_indices = []
                for i in indices:
                    if 0 <= i < len(archives):
                        selected_files.append(archives[i])
                    else:
                        invalid_indices.append(i + 1)

                if invalid_indices:
                    print(f"  无效序号: {invalid_indices}")

                if selected_files:
                    print(f"\n下载 {len(selected_files)} 个文件:")
                    for f in selected_files:
                        print(f"  - {f['name']}")
                    downloader.download_single_files(current_folder, selected_files, install_path)
            except ValueError:
                print("  无效输入")

    downloader.stats.stop()
    downloader.print_stats()


def main():
    share_url = "https://pan.nuaa.edu.cn/share/c5270595cf89e58b6d2ea76f28?page_number=1"

    print("=" * 50)
    print("南航云盘环境下载脚本")
    print("=" * 50)

    downloader = NuaaPanDownloader(share_url)

    # 获取文件夹列表
    print("\n获取文件夹列表...")
    folders = downloader.get_folders()

    if not folders:
        print("无法获取文件夹列表")
        return

    print(f"\n找到 {len(folders)} 个文件夹:")
    for i, f in enumerate(folders, 1):
        print(f"  {i}. {f['name']} ({downloader.format_size(f['size'])}, {f['item_count']}个文件)")

    # 选择模式
    print("\n" + "=" * 50)
    print("选择下载模式:")
    print("  1. 批量下载 - 选择文件夹，下载全部内容")
    print("  2. 选择性下载 - 进入文件夹，选择特定文件下载")
    print("=" * 50)

    mode = input("选择模式 (1/2): ").strip()

    if mode == '1':
        mode_batch_download(downloader, folders)
    elif mode == '2':
        mode_selective_download(downloader, folders)
    else:
        print("无效的选择")
        return

    print("\n完成!")


if __name__ == "__main__":
    main()
