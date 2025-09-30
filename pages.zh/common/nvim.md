# nvim

> Neovim，基于 Vim 的代码编辑器，使用多种不同的模式来修改文本。
> 在普通模式（normal mode）下，按下 `<i>` 键以进入插入模式（insert mode）。通过 `<Esc>` 或 `<Ctrl c>` 返回普通模式。普通模式下不支持一般的文本输入。
> 另见：`vim`，`vimtutor`，`vimdiff`。
> 更多信息：<https://neovim.io>.

- 打开文件:

`nvim {{path/to/file}}`

- 进入文本编辑模式（insert mode）：

`<Esc><i>`

- 复制（"yank"）或剪切（"delete"）当前行（使用 `<p>` 粘贴）：

`<Esc>{{<y><y>|<d><d>}}`

- 进入普通模式并撤消上次操作：

`<Esc><u>`

- 在当前文件中使用正则表达式搜索（使用 `<n>`/`<N>` 查看上一个/下一个搜索结果）：

`<Esc></>{{search_pattern}}<Enter>`

- 在当前文件中使用正则表达式进行全局替换：

`<Esc><:>%s/{{regular_expression}}/{{replacement}}/g<Enter>`

- 进入普通模式，保存文件并退出：

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- 退出并不保存更改

`<Esc><:>q!<Enter>`
