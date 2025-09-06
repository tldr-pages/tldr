# finger

> 返回有关指定系统上的一个或多个用户的信息。
> 远程系统必须运行 Finger 服务。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- 显示有关特定用户的信息：

`finger {{用户名}}@{{主机名}}`

- 在指定的主机上显示所有用户的信息：

`finger @{{主机名}}`

- 以更长的格式显示信息：

`finger {{用户名}}@{{主机名}} -l`

- 显示帮助信息：

`finger /?`
