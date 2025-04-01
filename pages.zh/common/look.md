# look

> 在已排序的文件中显示以指定前缀开头的行。
> 注意：文件中的行必须已排序。
> 参见：`grep`，`sort`。
> 更多信息：<https://man.openbsd.org/look>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{prefix}} {{path/to/file}}`

- 仅对字母数字字符进行不区分大小写的搜索：

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefix}} {{path/to/file}}`

- 指定字符串终止字符（默认为空格）：

`look {{[-t|--terminate]}} {{,}}`

- 在 `/usr/share/dict/words` 中搜索（假定 `--alphanum` 和 `--ignore-case`）：

`look {{prefix}}`