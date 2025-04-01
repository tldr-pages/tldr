# su

> 切换到另一个用户的身份。
> 更多信息：<https://manned.org/su>.

- 切换到超级用户（需要 root 密码）：

`su`

- 切换到指定用户（需要该用户的密码）：

`su {{username}}`

- 切换到指定用户并模拟完整的登录 shell：

`su - {{username}}`

- 以另一个用户的身份执行命令：

`su - {{username}} {{[-c|--command]}} "{{command}}"`