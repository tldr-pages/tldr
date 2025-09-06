# reg delete

> 从注册表中删除键和值。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- 删除一个指定的键：

`reg delete {{键名}}`

- 删除键中指定的值：

`reg delete {{键名}} /v {{值}}`

- 递归删除指定键下所有的值：

`reg delete {{键名}} /va`

- 在没有提示的情况下递归删除键中所有的值：

`reg delete {{键名}} /f /va`
