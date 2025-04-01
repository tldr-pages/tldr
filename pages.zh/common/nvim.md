# nvim

> Neovim 是基于 Vim 的程序员文本编辑器，提供了多种模式以进行不同类型的文字处理。
> 在正常模式下按 `<i>` 可以进入插入模式。使用 `<Esc>` 或 `<Ctrl c>` 可以返回到不允许普通文字插入的正常模式。
> 参见：`vim`，`vimtutor`，`vimdiff`。
> 更多信息：<https://neovim.io>。

- 打开文件：

`nvim {{path/to/file}}`

- 进入文本编辑模式（插入模式）：

`<Esc><i>`

- 复制（“yank”）或剪切（“delete”）当前行（用 `<p>` 粘贴）：

`<Esc>{{<y><y>|<d><d>}}`

- 进入正常模式并撤销上一个操作：

`<Esc><u>`

- 在文件中搜索模式（按 `<n>`/`<N>` 跳到下一个/上一个匹配项）：

`<Esc></>{{search_pattern}}<Enter>`

- 在整个文件中执行正则表达式替换：

`<Esc><:>%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 进入正常模式并保存（写入）文件且退出：

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- 不保存并退出：

`<Esc><:>q!<Enter>`