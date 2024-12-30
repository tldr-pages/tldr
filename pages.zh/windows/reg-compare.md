# reg compare

> 比较注册表中的键及其值。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>。

- 将特定键下的所有值与另一个键进行比较：

`reg compare {{key_name1}} {{key_name2}}`

- 比较两个键下的特定[v]alue：

`reg compare {{key_name1}} {{key_name2}} /v {{value}}`

- 比较两个键的所有[s]ubkeys和值：

`reg compare {{key_name1}} {{key_name2}} /s`

- 仅输出指定键之间的匹配项（[s]ame）：

`reg compare {{key_name1}} {{key_name2}} /os`

- 输出指定键之间的差异和匹配项（[a]ll）：

`reg compare {{key_name1}} {{key_name2}} /oa`

- 比较两个键，[o]utput不显示任何内容：

`reg compare {{key_name1}} {{key_name2}} /on`