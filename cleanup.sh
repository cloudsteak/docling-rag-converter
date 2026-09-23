#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
INPUT_DIR="$ROOT_DIR/input"
OUTPUT_DIR="$ROOT_DIR/output"

cleanup_dir_contents() {
  local dir="$1"

  if [[ -d "$dir" ]]; then
    find "$dir" -mindepth 1 ! -name ".gitkeep" -exec rm -rf -- {} +
  fi
}

if [[ -d "$VENV_DIR" ]]; then
  rm -rf -- "$VENV_DIR"
fi

cleanup_dir_contents "$INPUT_DIR"
cleanup_dir_contents "$OUTPUT_DIR"

echo "Cleanup complete."
