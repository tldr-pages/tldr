# usermod

> 修改用户账户。
> 相关命令：`users`, `useradd`, `userdel`。
> 更多信息：<https://manned.org/usermod>。

- 修改用户名：

`sudo usermod {{[-l|--login]}} {{new_username}} {{username}}`

- 修改用户ID：

`sudo usermod {{[-u|--uid]}} {{id}} {{username}}`

- 修改用户Shell：

`sudo usermod {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- 将用户添加到附加组（注意不要有空格）：

`sudo usermod {{[-aG|--append --groups]}} {{group1,group2,...}} {{username}}`

- 修改用户主目录：

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{path/to/new_home}} {{username}}`

- 锁定账户：

`sudo usermod {{[-L|--lock]}} {{username}}`

- 解锁账户：

`sudo usermod {{[-U|--unlock]}} {{username}}`