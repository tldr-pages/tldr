# gpasswd

> 管理 `/etc/group` 和 `/etc/gshadow`。
> 更多信息请访问: <https://manned.org/gpasswd>。

- 定义组管理员：

`sudo gpasswd -A {{user1,user2}} {{group}}`

- 设置组成员列表：

`sudo gpasswd -M {{user1,user2}} {{group}}`

- 为指定组创建密码：

`gpasswd {{group}}`

- 将用户添加到指定组：

`gpasswd -a {{user}} {{group}}`

- 从指定组中删除用户：

`gpasswd -d {{user}} {{group}}`