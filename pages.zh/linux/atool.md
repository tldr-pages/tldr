# atool

> 管理各种格式的归档文件。
> 更多信息：<https://manned.org/atool>。

- 列出 Zip 归档文件中的文件：

`atool {{[-l|--list]}} {{path/to/archive.zip}}`

- 解压缩 tar.gz 归档文件到一个新的子目录（如果归档中只有一个文件，则解压到当前目录）：

`atool {{[-x|--extract]}} {{path/to/archive.tar.gz}}`

- 创建一个包含两个文件的新 7z 归档文件：

`atool {{[-a|--add]}} {{path/to/archive.7z}} {{path/to/file1 path/to/file2 ...}}`

- 解压缩当前目录中的所有 Zip 和 rar 归档文件：

`atool {{[-e|--each]}} {{[-E|--extract]}} {{*.zip *.rar}}`
