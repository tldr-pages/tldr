# uuidparse

> 解析通用唯一标识符。
> 参见：`uuidgen`。
> 更多信息：<https://manned.org/uuidparse.1>。

- 解析指定的 UUID，使用表格输出格式：

`uuidparse {{uuid1 uuid2 ...}}`

- 从 `stdin` 解析 UUID：

`{{command}} | uuidparse`

- 使用 JSON 输出格式：

`uuidparse {{[-J|--json]}} {{uuid1 uuid2 ...}}`

- 不打印标题行：

`uuidparse {{[-n|--noheadings]}} {{uuid1 uuid2 ...}}`

- 使用原始输出格式：

`uuidparse {{[-r|--raw]}} {{uuid1 uuid2 ...}}`

- 指定要打印的四个输出列中的哪一个：

`uuidparse {{[-o|--output]}} {{UUID,VARIANT,TYPE,TIME}}`

- 显示帮助：

`uuidparse {{[-h|--help]}}`
