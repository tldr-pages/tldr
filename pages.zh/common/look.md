# look

> 在已排序的文件中显示以特定前缀开头的行。
> 注意：文件中的行必须是已排序的。
> 另见：`grep`、`sort`。
> 更多信息：<https://man.openbsd.org/look>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{prefix}} {{path/to/file}}`

- 不区分大小写（[f]）且仅在字母数字字符上搜索（[d]）：

`look -f -d {{prefix}} {{path/to/file}}`

- 指定字符串[t]ermination字符（默认是空格）：

`look -t {{,}}`

- 在`/usr/share/dict/words`中搜索（默认假定使用`-d`和`-f`）：

`look {{prefix}}`