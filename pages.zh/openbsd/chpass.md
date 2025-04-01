# chpass

> 添加或更改用户数据库信息，包括登录 shell 和密码。
> 参见：`passwd`。
> 更多信息：<https://man.openbsd.org/chsh>。

- 为当前用户交互式设置特定的登录 shell：

`doas chsh`

- 为当前用户设置特定的登录 [s]hell：

`doas chsh -s {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`doas chsh -s {{path/to/shell}} {{username}}`

- 指定 `passwd` 文件格式的用户数据库条目：

`doas chsh -a {{username:encrypted_password:uid:gid:...}}`