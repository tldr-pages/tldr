# reg save

> 将注册表项及其子项和值保存到本地 `.hiv` 文件中。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>。

- 将注册表项及其子项和值保存到指定文件：

`reg save {{key_name}} {{path\to\file.hiv}}`

- 强制覆盖现有文件（假设为[y]es）：

`reg save {{key_name}} {{path\to\file.hiv}} /y`