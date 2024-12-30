# reg query

> 显示注册表中键和子键的值。
> 更多信息: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>。

- 显示键的所有值：

`reg query {{key_name}}`

- 显示键的特定[v]alue：

`reg query {{key_name}} /v {{value}}`

- 显示键及其[s]ubkeys的所有值：

`reg query {{key_name}} /s`

- 搜索[f]or键和值以匹配特定模式：

`reg query {{key_name}} /f "{{query_pattern}}"`

- 显示匹配指定数据[t]ype的键的值：

`reg query {{key_name}} /t REG_{{SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE}}`

- 仅在[d]ata中搜索：

`reg query {{key_name}} /d`

- 仅在[k]ey名称中搜索：

`reg query {{key_name}} /f "{{query_pattern}}" /k`

- [c]区分大小写地搜索[e]xact匹配：

`reg query {{key_name}} /c /e`