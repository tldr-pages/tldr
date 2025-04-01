# chsh

> 更改用户的登录 shell。
> 属于 `util-linux` 包的一部分。
> 更多信息：<https://manned.org/chsh>。

- 交互式地为当前用户设置特定的登录 shell：

`chsh`

- 列出可用的 shell：

`chsh {{[-l|--list-shells]}}`

- 为当前用户设置特定的登录 shell：

`chsh {{[-s|--shell]}} {{path/to/shell}}`

- 为特定用户设置登录 shell：

`sudo chsh {{[-s|--shell]}} {{path/to/shell}} {{username}}`