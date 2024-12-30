# rgrep

> 使用正则表达式递归查找文件中的模式。
> 相当于 `grep -r`。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在当前工作目录递归搜索模式：

`rgrep "{{search_pattern}}"`

- 在当前工作目录递归搜索不区分大小写的模式：

`rgrep --ignore-case "{{search_pattern}}"`

- 在当前工作目录递归搜索扩展的正则表达式模式（支持 `?`、`+`、`{}`、`()` 和 `|`）：

`rgrep --extended-regexp "{{search_pattern}}"`

- 在当前工作目录递归搜索确切字符串（禁用正则表达式）：

`rgrep --fixed-strings "{{exact_string}}"`

- 在指定目录（或文件）递归搜索模式：

`rgrep "{{search_pattern}}" {{path/to/file_or_directory}}`