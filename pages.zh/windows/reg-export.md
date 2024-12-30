# reg export

> 将指定的子键和值导出到`.reg`文件中。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>。

- 导出特定键的所有子键和值：

`reg export {{key_name}} {{path\to\file.reg}}`

- 强制覆盖现有文件（假设[y]es）：

`reg export {{key_name}} {{path\to\file.reg}} /y`