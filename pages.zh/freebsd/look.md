# look

> 在排序文件中显示以特定前缀开头的行。
> 另见： `grep`, `sort`。
> 更多信息： <https://man.freebsd.org/cgi/man.cgi?look>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{前缀}} {{路径/到/文件}}`

- 仅对字母数字字符进行不区分大小写的搜索：

`look {{-f|--ignore-case}} {{-d|--alphanum}} {{前缀}} {{路径/到/文件}}`

- 指定字符串结束字符（默认是空格）：

`look {{-t|--terminate}} {{,}}`

- 在 `/usr/share/dict/words` 中搜索（假定使用 `--ignore-case` 和 `--alphanum`）：

`look {{前缀}}`