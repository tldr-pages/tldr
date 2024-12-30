# hledger 添加

> 在控制台中通过交互式提示记录新交易。
> 更多信息：<https://hledger.org/hledger.html#add>。

- 记录新交易，保存到默认的日记文件：

`hledger add`

- 向 `2024.journal` 添加交易，同时加载 `2023.journal` 以便补全：

`hledger add --file {{path/to/2024.journal}} --file {{path/to/2023.journal}}`

- 为前四个提示提供答案：

`hledger add {{today}} '{{best buy}}' {{expenses:supplies}} '{{$20}}'`

- 使用 `$PAGER` 显示 `add` 的选项和文档：

`hledger add --help`

- 如果可用，使用 `info` 或 `man` 显示 `add` 的文档：

`hledger help add`