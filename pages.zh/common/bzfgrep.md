# bzfgrep

> 在使用 `bzip2` 压缩的文件中使用 `fgrep` 查找由换行符分隔的固定字符串。
> 更多信息： <https://manned.org/bzfgrep>.

- 在压缩文件中查找与由换行符分隔的搜索字符串列表匹配的行（区分大小写）：

`bzfgrep "{{search_string}}" {{path/to/file}}`

- 在压缩文件中查找与由换行符分隔的搜索字符串列表匹配的行（不区分大小写）：

`bzfgrep --ignore-case "{{search_string}}" {{path/to/file}}`

- 在压缩文件中查找与由换行符分隔的搜索字符串列表不匹配的行：

`bzfgrep --invert-match "{{search_string}}" {{path/to/file}}`

- 为每个匹配项打印文件名和行号：

`bzfgrep --with-filename --line-number "{{search_string}}" {{path/to/file}}`

- 查找与模式匹配的行，仅打印匹配的文本：

`bzfgrep --only-matching "{{search_string}}" {{path/to/file}}`

- 在 bzip2 压缩的 tar 归档文件中递归查找给定的字符串列表：

`bzfgrep --recursive "{{search_string}}" {{path/to/file}}`
