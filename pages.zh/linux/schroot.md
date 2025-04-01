# schroot

> 以不同的根目录运行命令或启动交互式 shell。比 `chroot` 更具可定制性。
> 更多信息：<https://wiki.debian.org/Schroot>.

- 列出可用的 chroot 环境：

`schroot --list`

- 在特定的 chroot 环境中运行命令：

`schroot --chroot {{chroot}} {{command}}`

- 在特定的 chroot 环境中带选项运行命令：

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- 在所有可用的 chroot 环境中运行命令：

`schroot --all {{command}}`

- 作为特定用户在特定的 chroot 环境中启动交互式 shell：

`schroot --chroot {{chroot}} --user {{user}}`

- 开始一个新会话（在 `stdout` 上返回一个唯一的会话 ID）：

`schroot --begin-session --chroot {{chroot}}`

- 连接到现有的会话：

`schroot --run-session --chroot {{session_id}}`

- 结束现有的会话：

`schroot --end-session --chroot {{session_id}}`