# reg add

> 向注册表添加新键及其值。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>。

- 添加一个新的注册表键：

`reg add {{key_name}}`

- 在特定键下添加一个新的[v]alue：

`reg add {{key_name}} /v {{value}}`

- 添加一个具有特定[d]ata的新值：

`reg add {{key_name}} /d {{data}}`

- 向具有特定数据[t]ype的键添加一个新值：

`reg add {{key_name}} /t REG_{{SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ}}`

- [f]orcefully（无提示）覆盖现有的注册表值：

`reg add {{key_name}} /f`