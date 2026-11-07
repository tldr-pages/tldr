# reg add

> 将新的键值添加到注册表中。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>。

- 添加一个新的注册表键：

`reg add {{键名}}`

- 在指定的键下添加新值：

`reg add {{键名}} /v {{值}}`

- 添加一个具有指定数据的新值：

`reg add {{键名}} /d {{数据}}`

- 向具有特定数据类型的键添加新值：

`reg add {{键名}} /t REG_{{SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ}}`

- 在没有提示的情况下强制覆盖现有的注册表值：

`reg add {{键名}} /f`
