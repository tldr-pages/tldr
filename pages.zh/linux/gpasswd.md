# gpasswd

> 管理 `/etc/group` 和 `/etc/gshadow` 文件。
> 更多信息：<https://manned.org/gpasswd>。

- 定义组管理员：

`sudo gpasswd {{[-A|--administrators]}} {{user1,user2}} {{group}}`

- 设置组成员列表：

`sudo gpasswd {{[-M|--members]}} {{user1,user2}} {{group}}`

- 为指定组设置密码：

`gpasswd {{group}}`

- 将用户添加到指定组：

`gpasswd {{[-a|--add]}} {{user}} {{group}}`

- 从指定组中删除用户：

`gpasswd {{[-d|--delete]}} {{user}} {{group}}`
