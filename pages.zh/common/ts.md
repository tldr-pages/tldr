# ts

> 为每一行从 `stdin` 添加时间戳。
> 更多信息：<https://joeyh.name/code/moreutils/>。

- 在每一行的开头添加时间戳：

`{{command}} | ts`

- 添加具有微秒精度的时间戳：

`{{command}} | ts "{{%b %d %H:%M:%.S}}"`

- 从零开始添加具有微秒精度的[增量]时间戳：

`{{command}} | ts -i "{{%H:%M:%.S}}"`

- 将文本文件（例如日志文件）中现有的时间戳转换为[相对]格式：

`cat {{path/to/file}} | ts -r`