# run-mailcap

> 运行 MailCap 程序。
> 通过 mailcap 文件（或其别名）中的条目使用给定的动作处理每个 MIME 类型或文件。
> 更多信息：<https://manned.org/run-mailcap>.

- 可以使用动作标志调用 run-mailcap 上的单个动作/程序：

`run-mailcap --action=ACTION [--option[=value]]`

- 用简单的语言表示：

`run-mailcap --action=ACTION {{filename}}`

- 打开额外的信息：

`run-mailcap --action=ACTION --debug {{filename}}`

- 忽略任何 "copiousoutput" 指令并将输出转发到 `stdout`：

`run-mailcap --action=ACTION --nopager {{filename}}`

- 显示找到的命令但不实际执行它：

`run-mailcap --action=ACTION --norun {{filename}}`
