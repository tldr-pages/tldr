# finger

> 返回指定系统上用户的信息。
> 远程系统必须运行 Finger 服务。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/finger>。

- 显示特定用户的信息：

`finger {{user}}@{{host}}`

- 显示指定主机上所有用户的信息：

`finger @{{host}}`

- 以更长的格式显示信息：

`finger {{user}}@{{host}} -l`

- 显示帮助信息：

`finger /?`