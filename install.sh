#!/bin/bash
# =============================================
# OpenClaw Skills Installer
# Usage: bash install.sh
# =============================================
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET="$HOME/.openclaw-autoclaw/skills"

mkdir -p "$TARGET"

echo "🔗 Installing skills from: $SCRIPT_DIR"
echo "   Target: $TARGET"
echo ""

count=0

while IFS= read -r skill_file; do
  skill_dir="$(dirname "$skill_file")"
  rel_path="${skill_dir#$SCRIPT_DIR/}"
  skill_name="${rel_path//\//-}"

  [ -L "$TARGET/$skill_name" ] && rm -f "$TARGET/$skill_name"
  [ -d "$TARGET/$skill_name" ] && rm -rf "$TARGET/$skill_name"

  ln -sf "$skill_dir" "$TARGET/$skill_name"
  echo "  ✅ $skill_name"
  count=$((count + 1))
done < <(find "$SCRIPT_DIR" -name "SKILL.md" -not -path "*/references/*")

echo ""
echo "Done! Installed $count skills."

echo ""
echo "Linked skills:"
for d in "$TARGET"/*/; do
  name=$(basename "$d")
  if [ -L "$d" ]; then target=$(readlink "$d"); echo "  🔗 $name → $target"; else echo "  📁 $name"; fi
done
