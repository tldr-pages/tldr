# ex

> 命令行文本编辑器。
> 参见：`vim`。
> 更多信息：<https://www.vim.org>。

- 打开文件：

`ex {{path/to/file}}`

- 保存并退出：

`wq<Enter>`

- 撤销上一次操作：

`undo<Enter>`

- 在文件中搜索模式：

`/{{search_pattern}}<Enter>`

- 在整个文件中执行正则表达式替换：

`%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 插入文本：

`i<Enter>{{text}}<Ctrl c>`

- 切换到 Vim：

`visual<Enter>`