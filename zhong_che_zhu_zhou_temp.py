import os


def remove_license(file_path, num_lines=10):
    """删除文件顶部的指定行数（通常为 license 行）"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 假设 license 占据文件的前 num_lines 行
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines[num_lines:])


def process_directory(directory, num_lines=10, file_extension=".py"):
    """遍历目录并处理所有符合条件的文件"""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                remove_license(file_path, num_lines)


if __name__ == "__main__":
    # 指定你需要处理的目录和 license 行数
    directory_to_process = f"{os.getcwd()}/secsgem"
    license_line_count = 15  # 假设 license 占 10 行
    process_directory(directory_to_process, license_line_count)
