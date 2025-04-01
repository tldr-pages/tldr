# most

> 以交互方式打开一个或多个文件，允许滚动和搜索。
> 更多信息：<https://manned.org/most>.

- 打开一个文件：

`most {{path/to/file}}`

- 打开多个文件：

`most {{path/to/file1 path/to/file2 ...}}`

- 从包含"string"的第一个位置打开文件：

`most {{path/to/file}} +/{{string}}`

- 在打开的文件之间导航：

`<:><n>{{<上箭头>|<下箭头>}}`

- 跳转到第 100 行：

`<j>{{100}}<Enter>`

- 编辑当前文件：

`<e>`

- 将当前窗口分成两半：

`<CTRL x><o>`

- 退出：

`<q>`