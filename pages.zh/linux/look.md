# look

> 显示文件中以特定前缀开头的行。
> 注意：文件中的行必须是排序的。
> 参见：`grep`，`sort`。
> 更多信息：<https://manned.org/look>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{prefix}} {{path/to/file}}`

- 忽略大小写，仅在空白字符和字母数字字符上进行搜索：

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefix}} {{path/to/file}}`

- 指定字符串终止字符（默认为空格）：

`look {{[-t|--terminate]}} {{,}}`

- 在 `/usr/share/dict/words` 中搜索（默认启用 `--ignore-case` 和 `--alphanum`）：

`look {{prefix}}`

- 在 `/usr/share/dict/web2` 中搜索（默认启用 `--ignore-case` 和 `--alphanum`）：

`look {{[-a|--alternative]}} {{prefix}}`
