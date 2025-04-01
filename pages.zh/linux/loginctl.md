# loginctl

> 管理 systemd 登录管理器。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/loginctl.html>。

- 打印所有当前会话：

`loginctl list-sessions`

- 打印特定会话的所有属性：

`loginctl show-session {{session_id}} {{[-a|--all]}}`

- 打印特定用户的所有属性：

`loginctl show-user {{username}}`

- 打印用户的特定属性：

`loginctl show-user {{username}} {{[-p|--property]}} {{property_name}}`

- 在远程主机上执行 `loginctl` 操作：

`loginctl list-users {{[-H|--host]}} {{hostname}}`

- 注销用户的所有会话：

`loginctl terminate-user {{username}}`

- 显示帮助：

`loginctl {{[-h|--help]}}`
