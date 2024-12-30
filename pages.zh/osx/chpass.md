# chpass

> 添加或更改用户数据库信息，包括登录 shell 和密码。
> 注意：在 Open Directory 系统上无法更改用户的密码，请使用 `passwd`。
> 另见：`passwd`。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?chpass>。

- 交互式地为当前用户添加或更改用户数据库信息：

`su -c chpass`

- 为当前用户设置特定的登录 [s]hell：

`chpass -s {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`chpass -s {{path/to/shell}} {{username}}`

- 在给定 [l]ocation 的目录节点上编辑用户记录：

`chpass -l {{location}} -s {{path/to/shell}} {{username}}`

- 在对包含用户的目录节点进行身份验证时使用给定的 [u]sername：

`chpass -u {{authname}} -s {{path/to/shell}} {{username}}`