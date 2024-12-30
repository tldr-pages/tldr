# look

> 显示以特定前缀开头的行，来自一个已排序的文件。
> 另请参见：`grep`，`sort`。
> 更多信息：<https://keith.github.io/xcode-man-pages/look.1.html>。

- 在特定文件中搜索以特定前缀开头的行：

`look {{前缀}} {{路径/到/文件}}`

- 对字母数字字符进行不区分大小写的搜索：

`look {{-f|--ignore-case}} {{-d|--alphanum}} {{前缀}} {{路径/到/文件}}`

- 指定字符串终止字符（默认为空格）：

`look {{-t|--terminate}} {{字符}}`

- 在 `/usr/share/dict/words` 中搜索（假定使用 `--ignore-case` 和 `--alphanum`）：

`look {{前缀}}`