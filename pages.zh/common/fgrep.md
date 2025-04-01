# fgrep

> 在文件中匹配固定的字符串。
> 等效于 `grep -F`。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在文件中搜索一个固定的字符串：

`fgrep {{search_string}} {{path/to/file}}`

- 搜索一个或多个文件中完全匹配的行：

`fgrep {{[-x|--line-regexp]}} {{search_string}} {{path/to/file1 path/to/file2 ...}}`

- 统计文件中匹配给定字符串的行数：

`fgrep {{[-c|--count]}} {{search_string}} {{path/to/file}}`

- 显示匹配的行及其在文件中的行号：

`fgrep {{[-n|--line-number]}} {{search_string}} {{path/to/file}}`

- 显示所有不包含搜索字符串的行：

`fgrep {{[-v|--invert-match]}} {{search_string}} {{path/to/file}}`

- 显示内容至少一次匹配搜索字符串的文件名：

`fgrep {{[-l|--files-with-matches]}} {{search_string}} {{path/to/file1 path/to/file2 ...}}`
