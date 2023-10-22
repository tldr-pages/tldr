# reg flags

> 显示或设置注册表键的标志。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-flags>.

- 显示当前指定键的标志：

`reg flags {{键名}} query`

- 显示帮助和可用的标志类型：

`reg flags /?`

- 为特定键设置指定以空格分隔的标志，并取消设置未提及的标志：

`reg flags {{键名}} set {{标志 1 标志 2 ..}}`

- 为指定的键和其子键设置标志：

`reg flags {{键名}} set {{标志}} /s`
