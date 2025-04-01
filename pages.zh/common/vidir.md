# vidir

> 使用文本编辑器编辑目录。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 编辑指定目录的内容：

`vidir {{path/to/directory1 path/to/directory2 ...}}`

- 显示程序执行的每个操作：

`vidir --verbose {{path/to/directory1 path/to/directory2 ...}}`

- 编辑当前目录的内容：

`vidir`

- 使用指定的文本编辑器：

`EDITOR={{vim}} vidir {{path/to/directory1 path/to/directory2 ...}}`

- 从 `stdin` 读取要编辑的文件列表：

`{{command}} | vidir -`