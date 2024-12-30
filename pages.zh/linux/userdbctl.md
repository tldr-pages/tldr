# userdbctl

> 检查系统上的用户、组和组成员资格。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/userdbctl.html>。

- 列出所有已知的用户记录：

`userdbctl user`

- 显示特定用户的详细信息：

`userdbctl user {{用户名}}`

- 列出所有已知的组：

`userdbctl group`

- 显示特定组的详细信息：

`userdbctl group {{组名}}`

- 列出当前向系统提供用户/组定义的所有服务：

`userdbctl services`