# chpass

> 添加或更改用户数据库信息，包括登录 shell 和密码。
> 另见: `passwd`。
> 更多信息: <https://man.openbsd.org/chsh>。

- 以交互方式为当前用户设置特定的登录 shell：

`doas chsh`

- 为当前用户设置特定的登录 [s]hell：

`doas chsh -s {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`doas chsh -s {{path/to/shell}} {{username}}`

- 在 `passwd` 文件格式中指定用户数据库条目：

`doas chsh -a {{username:encrypted_password:uid:gid:...}}`