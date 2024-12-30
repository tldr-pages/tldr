# fgrep

> 在文件中匹配固定字符串。
> 等同于 `grep -F`。
> 更多信息：<https://www.gnu.org/software/grep/manual/grep.html>。

- 在文件中搜索精确字符串：

`fgrep {{search_string}} {{path/to/file}}`

- 仅搜索在一个或多个文件中完全匹配的行：

`fgrep -x {{search_string}} {{path/to/file1 path/to/file2 ...}}`

- 计算文件中与给定字符串匹配的行数：

`fgrep -c {{search_string}} {{path/to/file}}`

- 显示文件中匹配的行及其行号：

`fgrep -n {{search_string}} {{path/to/file}}`

- 显示所有不包含搜索字符串的行：

`fgrep -v {{search_string}} {{path/to/file}}`

- 显示内容中至少包含一次搜索字符串的文件名：

`fgrep -l {{search_string}} {{path/to/file1 path/to/file2 ...}}`