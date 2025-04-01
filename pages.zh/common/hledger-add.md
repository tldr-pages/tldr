# hledger add

> 在控制台中通过交互式提示记录新的交易。
> 更多信息：<https://hledger.org/hledger.html#add>.

- 记录新的交易，并保存到默认的记账文件：

`hledger add`

- 将交易添加到 `2024.journal`，同时加载 `2023.journal` 以提供补全：

`hledger add --file {{path/to/2024.journal}} --file {{path/to/2023.journal}}`

- 为前四个提示提供答案：

`hledger add {{today}} '{{best buy}}' {{expenses:supplies}} '{{$20}}'`

- 使用 `$PAGER` 显示 `add` 的选项和文档：

`hledger add --help`

- 使用 `info` 或 `man`（如果可用）显示 `add` 的文档：

`hledger help add`