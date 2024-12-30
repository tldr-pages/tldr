# yank

> 从 `stdin` 读取输入并显示选择界面，允许选择字段并复制到剪贴板。
> 更多信息：<https://manned.org/yank>。

- 使用默认分隔符（\f, \n, \r, \s, \t）进行 yank：

`{{sudo dmesg}} | yank`

- yank 整行：

`{{sudo dmesg}} | yank -l`

- 使用特定分隔符进行 yank：

`{{echo hello=world}} | yank -d {{=}}`

- 仅 yank 匹配特定模式的字段：

`{{ps ux}} | yank -g "{{[0-9]+}}"`