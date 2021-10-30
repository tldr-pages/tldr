# reg query

> 显示注册表中键和子键的值。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- 显示一个键中的所有值：

`reg query {{键名}}`

- 显示键中指定的值：

`reg query {{键名}} /v {{值}}`

- 显示指定键和其子键中的所有的值：

`reg query {{键名}} /s`

- 搜索与特定模式匹配的键和值：

`reg query {{键名}} /f "{{查询语句}}"`

- 显示与指定数据类型匹配的键的值：

`reg query {{键名}} /t {{类型}}`
