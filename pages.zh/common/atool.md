# atool

> 一个用于管理多种类型文件归档的脚本。
> `atool` 使用外部的归档程序，但提供了一个一致的命令行界面，用于列出、解压、创建和管理归档。
> 更多信息：<https://manned.org/atool>.

- 列出归档中的文件：

`atool {{[-l|--list]}} {{路径/到/归档.zip}}`

- 解压一个归档（如果需要，会安全地创建一个子目录）：

`atool {{[-x|--extract]}} {{archive.tar.gz}}`

- 将归档解压到指定目录：

`atool {{[-X|--extract-to]}} {{路径/到/输出_目录}} {{archive.rar}}`

- 将归档中某个特定文件的内容输出到 `stdout`（类似 `cat`）：

`atool {{[-c|--cat]}} {{archive.tar}} {{路径/到/归档中_文件.txt}}`

- 从指定的文件和 / 或目录创建一个新的归档：

`atool {{[-a|--add]}} {{new_archive.zip}} {{路径/到/文件1 路径/到/文件2 ...}}`

- 列出归档中的文件，并通过分页器输出结果：

`atool {{[-l|--list]}} {{[-p|--pager]}} {{large_archive.tar.bz2}}`

- 同时解压多个归档（如有需要，每个归档解压到各自的子目录中）：

`atool {{[-x|--extract]}} {{[-e|--each]}} {{archive1.zip}} {{archive2.tar.gz}} {{*.rar}}`

- 将归档从一种格式重新打包为另一种格式（例如 `.tar.gz` 转换为 `.tar.7z`）：

`atool {{[-r|--repack]}} {{old_archive.tar.gz}} {{new_archive.tar.7z}}`
