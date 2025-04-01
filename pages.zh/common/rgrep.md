# rgrep

> 使用正则表达式递归地在文件中查找模式。
> 等同于 `grep -r`。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html#Command_002dline-Options>。

- 递归地在当前工作目录中查找模式：

`rgrep "{{search_pattern}}"`

- 递归地在当前工作目录中查找不区分大小写的模式：

`rgrep {{[-i|--ignore-case]}} "{{search_pattern}}"`

- 递归地在当前工作目录中查找扩展正则表达式模式（支持 `?`、`+`、`{}`、`()` 和 `|`）：

`rgrep {{[-E|--extended-regexp]}} "{{search_pattern}}"`

- 递归地在当前工作目录中查找精确字符串（禁用正则表达式）：

`rgrep {{[-F|--fixed-strings]}} "{{exact_string}}"`

- 递归地在指定的目录（或文件）中查找模式：

`rgrep "{{search_pattern}}" {{path/to/file_or_directory}}`