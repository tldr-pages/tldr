# id3v2

> 管理 id3v2 标签，转换和列出 id3v1。
> 更多信息：<https://manned.org/id3v2.1>。

- 列出所有流派：

`id3v2 --list-genres`

- 列出特定文件的所有标签：

`id3v2 --list {{path/to/file1 path/to/file2 ...}}`

- 删除特定文件的 `id3v2` 或 `id3v1` 标签：

`id3v2 {{--delete-v2|--delete-v1}} {{path/to/file1 path/to/file2 ...}}`

- 显示帮助：

`id3v2 --help`

- 显示版本：

`id3v2 --version`