#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "notes.json")


def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note(title, body):
    notes = load_notes()
    notes.append({
        "title": title,
        "body": body,
        "created_at": datetime.now().isoformat()
    })
    save_notes(notes)
    print(f"已添加笔记: {title}")


def list_notes():
    notes = load_notes()
    if not notes:
        print("暂无笔记")
        return
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}  ({note['created_at']})")


def export_markdown(output_path=None):
    notes = load_notes()
    if not notes:
        print("暂无笔记可导出")
        return

    if output_path is None:
        output_path = os.path.join(os.path.dirname(__file__), "notes_export.md")

    lines = ["# 笔记导出\n"]
    for note in notes:
        lines.append(f"## {note['title']}\n")
        lines.append(f"*创建时间: {note['created_at']}*\n")
        lines.append(f"{note['body']}\n")
        lines.append("---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"已导出 {len(notes)} 条笔记到 {output_path}")


def main():
    if len(sys.argv) < 2:
        print("用法: python notes.py <命令>")
        print("命令:")
        print("  add <标题> <内容>   添加笔记")
        print("  list                列出所有笔记")
        print("  export [路径]       导出所有笔记为 markdown")
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 4:
            print("用法: python notes.py add <标题> <内容>")
            return
        add_note(sys.argv[2], sys.argv[3])

    elif cmd == "list":
        list_notes()

    elif cmd == "export":
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        export_markdown(output_path)

    else:
        print(f"未知命令: {cmd}")


if __name__ == "__main__":
    main()
