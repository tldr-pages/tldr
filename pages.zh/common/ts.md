# ts

> 为从 `stdin` 接收的每一行添加时间戳。
> 更多信息：<https://manned.org/ts>.

- 在每一行的开始添加时间戳：

`{{command}} | ts`

- 添加带有微秒精度的时间戳：

`{{command}} | ts "{{%b %d %H:%M:%.S}}"`

- 添加从零开始的带有微秒精度的[增]量时间戳：

`{{command}} | ts -i "{{%H:%M:%.S}}"`

- 将文本文件（例如日志文件）中的现有时间戳转换为[相]对格式：

`cat {{path/to/file}} | ts -r`
