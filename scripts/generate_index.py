import os

root = "context"
index_path = "index.md"

def collect_md_files(path):
    """递归收集 path 下所有 .md 文件路径"""
    md_files = []
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(".md") and file != "index.md":
                full_path = os.path.join(dirpath, file)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                md_files.append(rel_path)
    return sorted(md_files)

with open(index_path, "w", encoding="utf-8") as f:
    f.write("# 世界尽头的图书馆\n\n收录“绝对厉害”的作品")

    # 遍历 context 下的一级文件夹
    for folder in sorted(os.listdir(root)):
        folder_path = os.path.join(root, folder)
        if not os.path.isdir(folder_path):
            continue

        f.write(f"## {folder}\n\n")

        # 收集该一级目录下的所有 md 文件（包括子目录）
        md_files = collect_md_files(folder_path)
        for rel_path in md_files:
            title = os.path.splitext(os.path.basename(rel_path))[0]
            f.write(f"- [{title}]({rel_path})\n")
        f.write("\n")
