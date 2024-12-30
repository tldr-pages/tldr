# chsh

> 更改用户的登录 shell。
> 属于 `util-linux`。
> 更多信息：<https://manned.org/chsh>。

- 交互式地为当前用户设置特定的登录 shell：

`chsh`

- 为当前用户设置特定的登录 [s]hell：

`chsh --shell {{path/to/shell}}`

- 为特定用户设置登录 [s]hell：

`sudo chsh --shell {{path/to/shell}} {{username}}`

- [l]ist 可用的 shell：

`chsh --list-shells`