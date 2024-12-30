# 写

> 在指定已登录用户的终端上写消息（按 ctrl-C 停止写消息）。
> 使用 `who` 命令查找系统上所有活跃用户的所有终端_ID。另见 `mesg`。
> 更多信息：<https://manned.org/write>。

- 向指定终端 ID 的指定用户发送消息：

`write {{用户名}} {{终端_ID}}`

- 向终端 `/dev/tty/5` 上的 "testuser" 发送消息：

`write {{testuser}} {{tty/5}}`

- 向伪终端 `/dev/pts/5` 上的 "johndoe" 发送消息：

`write {{johndoe}} {{pts/5}}`