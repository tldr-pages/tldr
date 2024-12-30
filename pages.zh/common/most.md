# most

> 打开一个或多个文件进行交互式阅读，允许滚动和搜索。
> 更多信息：<https://manned.org/most>。

- 打开一个文件：

`most {{path/to/file}}`

- 打开多个文件：

`most {{path/to/file1 path/to/file2 ...}}`

- 在“字符串”的第一次出现处打开文件：

`most {{path/to/file}} +/{{string}}`

- 在打开的文件之间移动：

`:O n`

- 跳转到第100行：

`{{100}}j`

- 编辑当前文件：

`e`

- 将当前窗口分成两半：

`<CTRL-x> o`

- 退出：

`Q`