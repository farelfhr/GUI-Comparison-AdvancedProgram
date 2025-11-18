#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

run_app() {
  title="$1"
  script="$2"
  echo "Starting $title..."
  "$PYTHON_BIN" "$SCRIPT_DIR/$script" &
}

run_app "Tkinter Hello" "src/01_tkinter_hello.py"
run_app "Kivy Hello" "src/02_kivy_hello.py"
run_app "DearPyGui Hello" "src/03_dearpygui_hello.py"
run_app "Remi Hello" "src/04_remi_hello.py"

wait

