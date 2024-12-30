# usermod

> 修改用户账户。
> 另见: `users`, `useradd`, `userdel`。
> 更多信息: <https://manned.org/usermod>。

- 更改用户名：

`sudo usermod {{-l|--login}} {{new_username}} {{username}}`

- 更改用户ID：

`sudo usermod {{-u|--uid}} {{id}} {{username}}`

- 更改用户shell：

`sudo usermod {{-s|--shell}} {{path/to/shell}} {{username}}`

- 将用户添加到附加组（注意没有空格）：

`sudo usermod {{-a|--append}} {{-G|--groups}} {{group1,group2,...}} {{username}}`

- 更改用户主目录：

`sudo usermod {{-m|--move-home}} {{-d|--home}} {{path/to/new_home}} {{username}}`