# cp

> 复制文件和目录。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>。

- 将文件复制到另一个位置：

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- 将文件复制到另一个目录中，保持文件名不变：

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- 递归地将目录的内容复制到另一个位置（如果目标存在，目录将被复制到其中）：

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- 以详细模式递归复制目录（显示复制的文件）：

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- 一次性将多个文件复制到一个目录中：

`cp -t {{path/to/destination_directory}} {{path/to/file1 path/to/file2 ...}}`

- 以交互模式将所有特定扩展名的文件复制到另一个位置（在覆盖之前提示用户）：

`cp -i {{*.ext}} {{path/to/target_directory}}`

- 在复制之前跟随符号链接：

`cp -L {{link}} {{path/to/target_directory}}`

- 使用源文件的完整路径，在复制时创建任何缺失的中间目录：

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`