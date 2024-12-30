# vim

> Vim（Vi IMproved）是一个命令行文本编辑器，提供了多种模式以进行不同类型的文本操作。
> 在普通模式下按 `i` 进入插入模式。按 `<Esc>` 返回普通模式，这样就可以使用 Vim 命令。
> 另见： `vimdiff`，`vimtutor`，`nvim`。
> 更多信息：<https://www.vim.org>。

- 打开一个文件：

`vim {{path/to/file}}`

- 在指定行号打开一个文件：

`vim +{{line_number}} {{path/to/file}}`

- 查看 Vim 的帮助手册：

`:help<Enter>`

- 保存并退出当前缓冲区：

`{{<Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter>}}`

- 进入普通模式并撤销上一个操作：

`<Esc>u`

- 在文件中搜索模式（按 `n`/`N` 转到下一个/上一个匹配项）：

`/{{search_pattern}}<Enter>`

- 在整个文件中执行正则表达式替换：

`:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 显示行号：

`:set nu<Enter>`