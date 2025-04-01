# prosodyctl

> Prosody XMPP 服务器的控制工具。
> 注意：不建议通过 `prosodyctl` 进行进程管理。应使用系统提供的工具（例如 `systemctl`）。
> 更多信息：<https://prosody.im/doc/prosodyctl>。

- 显示 Prosody 服务器的状态：

`sudo prosodyctl status`

- 重新加载服务器的配置文件：

`sudo prosodyctl reload`

- 向 Prosody XMPP 服务器添加用户：

`sudo prosodyctl adduser {{user@example.com}}`

- 设置用户的密码：

`sudo prosodyctl passwd {{user@example.com}}`

- 永久删除用户：

`sudo prosodyctl deluser {{user@example.com}}`
