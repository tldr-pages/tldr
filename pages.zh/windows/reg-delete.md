# reg delete

> 从注册表中删除键或它们的值。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>。

- 删除特定的注册表键：

`reg delete {{key_name}}`

- 删除特定键下的 [v]alue：

`reg delete {{key_name}} /v {{value}}`

- 递归删除指定键下的 [a]ll [v]alues：

`reg delete {{key_name}} /va`

- [f]orcefully（无需提示）递归删除键下的 [a]ll [v]alues：

`reg delete {{key_name}} /f /va`