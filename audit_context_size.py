#!/usr/bin/env python3
"""Scan a repository to highlight large folders and files that can consume
Google Antigravity 5-hour rolling context quota unnecessarily.
"""
import os
import sys

SKIP_GIT = {".git"}

def human_size(num: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if num < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} TB"

def scan(root: str) -> None:
    folder_sizes = {}
    large_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_GIT]
        total = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                sz = os.path.getsize(fp)
            except OSError:
                continue
            total += sz
            if sz >= 512 * 1024:
                large_files.append((sz, os.path.relpath(fp, root)))
        rel = os.path.relpath(dirpath, root)
        top = rel.split(os.sep)[0]
        folder_sizes[top] = folder_sizes.get(top, 0) + total

    print("Top directories by disk size (consider excluding build/vendor dirs in .antigravityignore):")
    for name, sz in sorted(folder_sizes.items(), key=lambda x: -x[1])[:12]:
        print(f"  {human_size(sz):>10}  {name}")

    if large_files:
        print("\nFiles >= 512 KB:")
        for sz, rel in sorted(large_files, reverse=True)[:15]:
            print(f"  {human_size(sz):>10}  {rel}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    scan(os.path.abspath(target))
