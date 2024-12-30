# zfgrep

> 在可能被压缩的文件中匹配固定字符串。
> 相当于首先解压输入后再使用 `grep -F`。
> 更多信息请访问: <https://manned.org/zfgrep>。

- 在文件中搜索确切字符串：

`zfgrep {{search_string}} {{path/to/file}}`

- 计算文件中与给定字符串匹配的行数：

`zfgrep --count {{search_string}} {{path/to/file}}`

- 显示文件中的行号和匹配的行：

`zfgrep --line-number {{search_string}} {{path/to/file}}`

- 显示所有不包含搜索字符串的行：

`zfgrep --invert-match {{search_string}} {{path/to/file}}`

- 仅列出内容至少匹配搜索字符串一次的文件名：

`zfgrep --files-with-matches {{search_string}} {{path/to/file1 path/to/file2 ...}}`