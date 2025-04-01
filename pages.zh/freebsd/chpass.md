# chpass

> 添加或更改用户数据库信息，包括登录 shell 和密码。
> 参见：`passwd`。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?chpass>。

- 交互式地为当前用户添加或更改用户数据库信息：

`su -c chpass`

- 为当前用户设置特定的登录 [s]hell：

`chpass -s {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`chpass -s {{path/to/shell}} {{username}}`

- 更改账户的 [e]xpire 时间（从 UTC 时间纪元开始的秒数）：

`su -c 'chpass -e {{time}} {{username}}'`

- 更改用户的密码：

`su -c 'chpass -p {{encrypted_password}} {{username}}'`

- 指定要查询的 NIS 服务器的 [h]ostname 或地址：

`su -c 'chpass -h {{hostname}} {{username}}'`

- 指定特定的 NIS [d]omain（默认为系统域名）：

`su -c 'chpass -d {{domain}} {{username}}'`