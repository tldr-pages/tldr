# yank

> 从 `stdin` 读取输入并显示一个选择界面，该界面允许选择一个字段并将其复制到剪贴板。
> 更多信息：<https://manned.org/yank>.

- 使用默认分隔符（\f, \n, \r, \s, \t）：

`{{sudo dmesg}} | yank`

- 输入单行：

`{{sudo dmesg}} | yank -l`

- 使用特定分 `=` 隔符输入：

`{{echo hello=world}} | yank -d {{=}}`

- 只有与特定正则表达式匹配的内容才输入：

`{{ps ux}} | yank -g "{{[0-9]+}}"`
