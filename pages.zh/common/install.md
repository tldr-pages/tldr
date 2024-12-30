# 安装

> 复制文件并设置属性。
> 将文件（通常是可执行文件）复制到系统位置，例如 `/usr/local/bin`，并赋予适当的权限/所有权。
> 更多信息请访问：<https://www.gnu.org/software/coreutils/install>。

- 将文件复制到目标位置：

`install {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- 将文件复制到目标位置，并设置它们的所有权：

`install --owner {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- 将文件复制到目标位置，并设置它们的组所有权：

`install --group {{user}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- 将文件复制到目标位置，并设置它们的 `mode`：

`install --mode {{+x}} {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- 复制文件并将源文件的访问/修改时间应用到目标文件：

`install --preserve-timestamps {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`

- 复制文件并在目标位置创建目录（如果不存在）：

`install -D {{path/to/source_file1 path/to/source_file2 ...}} {{path/to/destination}}`