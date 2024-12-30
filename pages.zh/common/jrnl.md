# jrnl

> 一个简单的命令行日记应用程序。
> 更多信息：<https://jrnl.sh>。

- 使用您的编辑器插入新条目：

`jrnl`

- 快速插入新条目：

`jrnl {{今天凌晨3点}}: {{标题}}. {{内容}}`

- 查看最近的十个条目：

`jrnl -n {{10}}`

- 查看从去年年初到去年三月初发生的所有事情：

`jrnl -from "{{去年}}" -until {{三月}}`

- 编辑所有标记为“texas”和“history”的条目：

`jrnl {{@texas}} -and {{@history}} --edit`