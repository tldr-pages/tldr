# jrnl

> 一个简单的命令行日记应用程序。
> 更多信息：<https://jrnl.sh>.

- 使用编辑器插入一个新条目：

`jrnl`

- 快速插入一个新条目：

`jrnl {{today at 3am}}: {{标题}}. {{内容}}`

- 查看最近的十条条目：

`jrnl -n {{10}}`

- 查看从去年开始到今年三月初所有发生的事情：

`jrnl -from "{{last year}}" -until {{march}}`

- 编辑所有用 "texas" 和 "history" 标签标记的条目：

`jrnl {{@texas}} -and {{@history}} --edit`
