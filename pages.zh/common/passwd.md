# passwd

> 更改用户的密码。
> 更多信息：<https://manned.org/passwd>.

- 交互式更改当前用户的密码：

`passwd`

- 更改特定用户的密码：

`passwd {{username}}`

- 获取用户的当前状态：

`passwd {{[-S|--status]}}`

- 将账户的密码设为空（会使指定账户无密码）：

`passwd {{[-d|--delete]}}`

- 以编程方式设置密码（适合安装脚本使用）：

`yes {{password}} | passwd`