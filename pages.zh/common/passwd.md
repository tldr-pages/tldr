# passwd

> 更改用户密码。
> 另请参阅：`chpasswd`。
> 更多信息：<https://manned.org/passwd>。

- 交互式更改当前用户的密码：

`passwd`

- 更改特定用户的密码：

`sudo passwd {{用户名}}`

- 获取用户当前状态：

`passwd {{[-S|--status]}}`

- 将账户密码设置为空（将使该账户无密码）：

`passwd {{[-d|--delete]}}`

- 以编程方式设置密码（适用于安装脚本）：

`yes {{密码}} | passwd`
