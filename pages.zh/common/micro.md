# micro

> 一个现代且直观的基于终端的文本编辑器。
> 您可以使用键盘，也可以使用鼠标来导航和/或选择文本。
> 更多信息：<https://micro-editor.github.io>。

- 打开一个文件：

`micro {{path/to/file}}`

- 保存一个文件：

`<Ctrl> + S`

- 剪切整行：

`<Ctrl> + K`

- 在文件中搜索模式（按 `Ctrl + N`/`Ctrl + P` 跳转到下一个/上一个匹配项）：

`<Ctrl> + F "{{pattern}}" <Enter>`

- 执行命令：

`<Ctrl> + E {{command}} <Enter>`

- 在整个文件中进行替换：

`<Ctrl> + E replaceall "{{pattern}}" "{{replacement}}" <Enter>`

- 退出：

`<Ctrl> + Q`