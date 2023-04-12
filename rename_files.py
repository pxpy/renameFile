import os

# 获取用户输入的目标文件夹路径、旧文件头和新文件头
folder_path = input("请输入目标文件夹路径：")
old_prefix = input("请输入旧文件头：")
new_prefix = input("请输入新文件头：")

# 递归修改文件名函数
def rename_files(folder_path, old_prefix, new_prefix):
    # 获取目标文件夹下的所有文件名和子文件夹名
    entries = os.listdir(folder_path)

    # 遍历所有文件名和子文件夹名
    for entry in entries:
        full_path = os.path.join(folder_path, entry)

        # 如果是文件，则尝试重命名
        if os.path.isfile(full_path) and entry.startswith(old_prefix):
            new_file_name = new_prefix + entry[len(old_prefix):]
            os.rename(full_path, os.path.join(folder_path, new_file_name))

        # 如果是子文件夹，则递归调用本函数
        elif os.path.isdir(full_path):
            rename_files(full_path, old_prefix, new_prefix)

# 递归修改文件名
rename_files(folder_path, old_prefix, new_prefix)
