# atool

> 管理各种格式的档案。
> 更多信息：<https://www.nongnu.org/atool/>。

- 列出 Zip 档案中的文件：

`atool --list {{path/to/archive.zip}}`

- 将 tar.gz 档案解压到一个新子目录中（如果只包含一个文件，则解压到当前目录）：

`atool --extract {{path/to/archive.tar.gz}}`

- 创建一个包含两个文件的新 7z 档案：

`atool --add {{path/to/archive.7z}} {{path/to/file1 path/to/file2 ...}}`

- 解压当前目录中的所有 Zip 和 rar 档案：

`atool --each --extract {{*.zip *.rar}}`