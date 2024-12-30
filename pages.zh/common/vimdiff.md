# vimdiff

> 在vim中打开两个或更多文件，并显示它们之间的差异。
> 另见: `vim`, `vimtutor`, `nvim`。
> 更多信息: <https://www.vim.org>。

- 打开两个文件并显示差异：

`vimdiff {{path/to/file1}} {{path/to/file2}}`

- 将光标移动到左侧|右侧窗口：

`<Ctrl> + w {{h|l}}`

- 跳转到上一个差异：

`[c`

- 跳转到下一个差异：

`]c`

- 将高亮的差异从另一个窗口复制到当前窗口：

`do`

- 将高亮的差异从当前窗口复制到另一个窗口：

`dp`

- 更新所有高亮和折叠：

`:diffupdate`

- 切换高亮代码的折叠：

`za`