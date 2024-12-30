# bzfgrep

> 使用 `fgrep` 在 `bzip2` 压缩文件中查找以新行分隔的固定字符串。
> 更多信息：<https://manned.org/bzfgrep>。

- 在压缩文件中搜索匹配以新行分隔的搜索字符串列表的行（区分大小写）：

`bzfgrep "{{search_string}}" {{path/to/file}}`

- 在压缩文件中搜索匹配以新行分隔的搜索字符串列表的行（不区分大小写）：

`bzfgrep --ignore-case "{{search_string}}" {{path/to/file}}`

- 在压缩文件中搜索不匹配以新行分隔的搜索字符串列表的行：

`bzfgrep --invert-match "{{search_string}}" {{path/to/file}}`

- 为每个匹配打印文件名和行号：

`bzfgrep --with-filename --line-number "{{search_string}}" {{path/to/file}}`

- 搜索匹配模式的行，仅打印匹配的文本：

`bzfgrep --only-matching "{{search_string}}" {{path/to/file}}`

- 递归搜索 bzip2 压缩的 tar 存档中的文件，查找给定字符串列表：

`bzfgrep --recursive "{{search_string}}" {{path/to/file}}`