# 文件名批量修改脚本

本脚本可以递归地遍历指定目录下的所有文件和子目录，并将所有以指定前缀开头的文件名修改为以新的前缀开头的文件名。

## 用法

1. 下载 `rename_files.py` 脚本文件。

2. 在终端或命令提示符中运行 Python 解释器，并使用 `cd` 命令进入脚本文件所在的目录。

3. 在终端或命令提示符中输入以下命令并按 Enter 键：

   ```sh
   python rename_files.py
   ```

4. 脚本将提示您输入以下参数：

   - 目标文件夹路径：要修改文件名的目标文件夹的路径。
   - 旧文件头：要修改的文件名的旧前缀。
   - 新文件头：要修改的文件名的新前缀。

5. 输入所需的参数并按 Enter 键。脚本将执行递归文件名修改操作。

## 注意事项

- 请确保输入的目标文件夹路径是正确的，以避免意外删除或修改文件。
- 请确保输入的旧文件头和新文件头是正确的，并且符合您的修改需求。
- 在操作前，请务必备份您的数据，以避免数据丢失。
