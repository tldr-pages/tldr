# write

> 向指定登录用户发送消息（`<Ctrl c>` 可停止发送消息）。
> 使用 `who` 命令查看系统中所有活动用户的终端 ID。另见 `mesg`。
> 更多信息：<https://manned.org/write>.

- 向指定用户在指定的终端 ID 上发送消息：

`write {{username}} {{terminal_id}}`

- 向终端 `/dev/tty/5` 上的用户 "testuser" 发送消息：

`write {{testuser}} {{tty/5}}`

- 向伪终端 `/dev/pts/5` 上的用户 "johndoe" 发送消息：

`write {{johndoe}} {{pts/5}}`
