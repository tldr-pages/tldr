# chpass

> 添加或更改用户数据库信息，包括登录 shell 和密码。
> 参见：`passwd`。
> 更多信息：<https://man.netbsd.org/chsh>。

- 为当前用户交互式设置特定的登录 shell：

`su -c chpass`

- 为当前用户设置特定的登录 [s]hell：

`chpass -s {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`chpass -s {{path/to/shell}} {{username}}`

- 在 `passwd` 文件格式中指定用户数据库条目：

`su -c 'chpass -a {{username:encrypted_password:uid:gid:...}} -s {{path/to/file}}' {{username}}`

- 仅更新 [l]ocal 密码文件：

`su -c 'chpass -l -s {{path/to/shell}}' {{username}}`

- 强制更改数据库 [y]P 密码数据库条目：

`su -c 'chpass -y -s {{path/to/shell}}' {{username}}`