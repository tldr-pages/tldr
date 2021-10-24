# reg compare

> 比较注册表中的键和值。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- 比较两个键中的所有值：

`reg compare {{第一个键名}} {{第二个键名}}`

- 比较两个键中指定的值：

`reg compare {{第一个键名}} {{第二个键名}} /v {{值}}`

- 比较两个键中的所有子键和值：

`reg compare {{第一个键名}} {{第二个键名}} /s`

- 仅输出指定键之间匹配的结果：

`reg compare {{第一个键名}} {{第二个键名}} /os`

- 输出两个键之间的匹配和差异：

`reg compare {{第一个键名}} {{第二个键名}} /oa`
