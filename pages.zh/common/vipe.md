# vipe

> 在 UNIX 管道中间运行文本编辑器。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 在将 `command1` 的输出通过管道传递给 `command2` 之前进行编辑：

`{{command1}} | vipe | {{command2}}`

- 将 `command1` 的输出缓冲到具有指定文件扩展名的临时文件中，以便帮助语法高亮：

`{{command1}} | vipe --suffix {{json}} | {{command2}}`

- 使用指定的文本编辑器：

`{{command1}} | EDITOR={{vim}} vipe | {{command2}}`