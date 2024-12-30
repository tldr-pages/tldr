# run-mailcap

> 运行 MailCap 程序。
> 运行 mailcap 查看、编辑、撰写、打印 - 通过 mailcap 文件（或其任何别名）中的条目执行程序，使用给定的操作处理每种 mime 类型/文件。
> 更多信息：<https://manned.org/run-mailcap>。

- 可以通过操作标志调用 run-mailcap 上的各个操作/程序：

`run-mailcap --action=ACTION [--option[=value]]`

- 简单来说：

`run-mailcap --action=ACTION {{filename}}`

- 打开额外信息：

`run-mailcap --action=ACTION --debug {{filename}}`

- 忽略任何 "copiousoutput" 指令并将输出转发到 `stdout`：

`run-mailcap --action=ACTION --nopager {{filename}}`

- 显示找到的命令而不实际执行它：

`run-mailcap --action=ACTION --norun {{filename}}`