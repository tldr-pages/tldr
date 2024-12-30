# reg restore

> 从本地 `.hiv` 文件恢复一个键及其值。
> 有关更多信息，请参见 `reg-save`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-restore>。

- 用备份文件中的数据覆盖指定的键：

`reg restore {{key_name}} {{path\to\file.hiv}}`