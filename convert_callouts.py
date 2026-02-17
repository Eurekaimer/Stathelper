import os
import re

# 配置你的文档目录
DOCS_DIR = "docs"

# 你提供的所有类型列表 (脚本会用来做验证，确保不误伤普通引用)
# 这些会被转换为小写的 !!! type
SUPPORTED_TYPES = {
    "note", "abstract", "info", "tip", "success", "question",
    "warning", "failure", "danger", "bug", "example", "quote",
    "tldr"
}

# 正则匹配： > [!TYPE] Title
# Group 1: 类型 (不区分大小写)
# Group 2: 标题 (可选)
CALLOUT_PATTERN = re.compile(r'^>\s*\[!([a-zA-Z]+)\]\s*(.*)$')

def process_file(filepath):
    # 读取文件
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_callout = False      # 标记：当前是否处于 callout 块中
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        
        # --- 1. 检查是否是 Callout 的标题行 (例如: > [!NOTE] 标题) ---
        match = CALLOUT_PATTERN.match(line)
        if match:
            # 提取类型并转小写 (例如 NOTE -> note)
            raw_type = match.group(1).lower()
            title = match.group(2).strip()
            
            # 只有当你列表里的类型才转换，避免误伤其他奇怪的自定义写法
            if raw_type in SUPPORTED_TYPES:
                # 构造 MkDocs 格式头部
                if title:
                    # 有标题：!!! note "标题"
                    new_lines.append(f'!!! {raw_type} "{title}"\n')
                else:
                    # 无标题：!!! note
                    new_lines.append(f'!!! {raw_type}\n')
                
                in_callout = True
                continue
            # 如果不在支持列表里，就按普通引用处理，继续往下走...

        # --- 2. 处理 Callout 块内的内容行 ---
        if in_callout:
            # Case A: 这一行还是以 > 开头，说明还在引用块里
            if stripped_line.startswith('>'):
                # 去掉开头的 >，并清理两边的空白（保留中间的空格）
                # 注意：这里我们只去掉第一个 > 和紧随其后的一个空格
                content = line.lstrip().lstrip('>').rstrip()
                if content.startswith(' '):
                    content = content[1:]
                
                # 必须缩进 4 个空格！！这是 MkDocs 识别的关键
                if not content:
                    # 如果是空行，只要换行符
                    new_lines.append('\n')
                else:
                    new_lines.append(f'    {content}\n')
            
            # Case B: 空行
            # GitHub Markdown 中，引用块中间的空行通常没有 >
            # 但在 MkDocs 中，这行也需要保持缩进或留空
            elif stripped_line == "":
                new_lines.append('\n')
            
            # Case C: 遇到非 > 开头的非空行 -> Callout 结束
            else:
                in_callout = False
                new_lines.append(line)
        
        # --- 3. 普通行 (不在 Callout 里) ---
        else:
            new_lines.append(line)

    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"✅ 已转换: {filepath}")

def main():
    print(f"正在扫描目录: {DOCS_DIR} ...")
    print(f"支持转换的类型: {', '.join(SUPPORTED_TYPES)}")
    
    count = 0
    # 递归遍历所有子目录
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))
                count += 1
    
    print(f"\n🎉 处理完成！共扫描 {count} 个 Markdown 文件。")

if __name__ == "__main__":
    main()