# nvim

> Neovim 是一个基于 Vim 的程序员文本编辑器，提供了多种模式以进行不同类型的文本操作。
> 在普通模式下按 `i` 进入插入模式。`<Esc>` 返回普通模式，此模式不允许常规文本插入。
> 另见：`vim`、`vimtutor`、`vimdiff`。
> 更多信息：<https://neovim.io>。

- 打开一个文件：

`nvim {{path/to/file}}`

- 进入文本编辑模式（插入模式）：

`<Esc>i`

- 复制（“揩”）或剪切（“删除”）当前行（用 `P` 粘贴）：

`<Esc>{{yy|dd}}`

- 进入普通模式并撤销上一个操作：

`<Esc>u`

- 在文件中搜索模式（按 `n`/`N` 转到下一个/上一个匹配项）：

`<Esc>/{{search_pattern}}<Enter>`

- 在整个文件中执行正则表达式替换：

`<Esc>:%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 进入普通模式并保存（写入）文件，然后退出：

`{{<Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter>}}`

- 不保存退出：

`<Esc>:q!<Enter>`