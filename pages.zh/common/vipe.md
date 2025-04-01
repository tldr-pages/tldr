# vipe

> 在 UNIX 管道中运行文本编辑器。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 编辑 `command1` 的输出，然后将其传递给 `command2`：

`{{command1}} | vipe | {{command2}}`

- 使用指定的文件扩展名将 `command1` 的输出缓冲到临时文件中，以辅助语法高亮：

`{{command1}} | vipe --suffix {{json}} | {{command2}}`

- 使用指定的文本编辑器：

`{{command1}} | EDITOR={{vim}} vipe | {{command2}}`