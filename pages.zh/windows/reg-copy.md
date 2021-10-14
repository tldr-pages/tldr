# reg copy

> 复制注册表中的键和值。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- 将注册表键复制到新的注册表位置：

`reg copy {{旧键名}} {{新键名}}`

- 递归将注册表键复制到新的注册表位置：

`reg copy {{旧键名}} {{新键名}} /s`

- 在没有提示的情况下强制复制注册表键：

`reg copy {{旧键名}} {{新键名}} /f`
