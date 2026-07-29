# atool

> 管理各种类型文件归档的脚本。
> `atool` 使用外部归档程序，但为列出、提取、创建和管理归档提供了一致的命令行接口。
> 更多信息：<https://manned.org/atool>。

- 列出归档中的文件：

`atool {{[-l|--list]}} {{路径/到/archive.zip}}`

- 提取归档（如果需要则安全创建子目录）：

`atool {{[-x|--extract]}} {{archive.tar.gz}}`

- 将归档提取到指定目录：

`atool {{[-X|--extract-to]}} {{路径/到/输出目录}} {{archive.rar}}`

- 将归档中特定文件的内容显示到 `stdout`（如 `cat`）：

`atool {{[-c|--cat]}} {{archive.tar}} {{路径/到/archive_中的文件.txt}}`

- 从指定文件和/或目录创建新归档：

`atool {{[-a|--add]}} {{new_archive.zip}} {{路径/到/文件1 路径/到/文件2 ...}}`

- 列出归档中的文件并通过分页器发送输出：

`atool {{[-l|--list]}} {{[-p|--pager]}} {{large_archive.tar.bz2}}`

- 同时提取多个归档（每个到其子目录）：

`atool {{[-x|--extract]}} {{[-e|--each]}} {{archive1.zip}} {{archive2.tar.gz}} {{*.rar}}`

- 将归档从一种格式重新打包为另一种格式（如 `.tar.gz` 到 `.tar.7z`）：

`atool {{[-r|--repack]}} {{old_archive.tar.gz}} {{new_archive.tar.7z}}`
