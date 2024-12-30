# Helix

> Helix，一个后现代文本编辑器，提供多种模式以便于不同类型的文本操作。
> 按 `i` 进入插入模式。`<Esc>` 进入普通模式，这时可以使用 Helix 命令。
> 更多信息请访问: <https://helix-editor.com>。

- 打开一个文件：

`helix {{path/to/file}}`

- 并排打开文件并显示它们：

`helix --vsplit {{path/to/file1 path/to/file2}}`

- 显示学习 Helix 的教程（或在 Helix 中按 `<Esc>` 并输入 `:tutor` 访问）：

`helix --tutor`

- 更改 Helix 主题：

`:theme {{theme_name}}`

- 保存并退出：

`:wq<Enter>`

- 强制退出而不保存：

`:q!<Enter>`

- 撤销上一步操作：

`u`

- 在文件中搜索模式（按 `n`/`N` 跳转到下一个/上一个匹配项）：

`/{{search_pattern}}<Enter>`