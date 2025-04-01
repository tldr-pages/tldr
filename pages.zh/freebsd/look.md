# look

> 在排序后的文件中显示以特定前缀开头的行。
> 参见: `grep`, `sort`。
> 更多信息: <https://man.freebsd.org/cgi/man.cgi?look>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{prefix}} {{path/to/file}}`

- 仅在字母数字字符上进行不区分大小写的搜索：

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefix}} {{path/to/file}}`

- 指定字符串终止字符（默认为空格）：

`look {{[-t|--terminate]}} {{,}}`

- 在 `/usr/share/dict/words` 中搜索（假设使用 `--ignore-case` 和 `--alphanum`）：

`look {{prefix}}`