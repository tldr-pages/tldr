# schroot

> 在不同的根目录下运行命令或启动交互式shell。比`chroot`更具可定制性。
> 更多信息：<https://wiki.debian.org/Schroot>。

- 列出可用的chroot：

`schroot --list`

- 在特定的chroot中运行命令：

`schroot --chroot {{chroot}} {{command}}`

- 在特定的chroot中运行带选项的命令：

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- 在所有可用的chroot中运行命令：

`schroot --all {{command}}`

- 以特定用户在特定的chroot中启动交互式shell：

`schroot --chroot {{chroot}} --user {{user}}`

- 开始一个新会话（在`stdout`上返回一个唯一的会话ID）：

`schroot --begin-session --chroot {{chroot}}`

- 连接到现有会话：

`schroot --run-session --chroot {{session_id}}`

- 结束现有会话：

`schroot --end-session --chroot {{session_id}}`