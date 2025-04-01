# userdbctl

> 检查系统中的用户、组和组成员关系。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/userdbctl.html>。

- 列出所有已知的用户记录：

`userdbctl user`

- 显示特定用户的详细信息：

`userdbctl user {{username}}`

- 列出所有已知的组：

`userdbctl group`

- 显示特定组的详细信息：

`userdbctl group {{groupname}}`

- 列出当前为系统提供用户/组定义的所有服务：

`userdbctl services`
