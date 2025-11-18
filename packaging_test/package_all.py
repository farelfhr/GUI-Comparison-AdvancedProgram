# Simple helper to build standalone executables with PyInstaller.
# Usage:
#   cd packaging_test
#   python package_all.py

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

TARGETS = [
    ("Tkinter Hello", SRC / "01_tkinter_hello.py"),
    ("Kivy Hello", SRC / "02_kivy_hello.py"),
    ("DearPyGui Hello", SRC / "03_dearpygui_hello.py"),
    ("Remi Hello", SRC / "04_remi_hello.py"),
]


def build_all() -> None:
    for title, script in TARGETS:
        print(f"\n=== Building {title} ===")
        cmd = [
            "pyinstaller",
            "--onefile",
            "--noconfirm",
            "--distpath",
            str(Path.cwd() / "dist"),
            "--workpath",
            str(Path.cwd() / "build"),
            str(script),
        ]
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    build_all()

