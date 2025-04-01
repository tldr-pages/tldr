# hledger-ui

> `hledger` 的终端界面 (TUI)，`hledger` 是一个强大且友好的纯文本会计应用程序。
> 更多信息：<https://hledger.org/hledger-ui.html>.

- 从默认的记账文件读取，进入主菜单屏幕：

`hledger-ui`

- 使用不同的颜色主题启动：

`hledger-ui --theme {{terminal|greenterm|dark}}`

- 进入资产负债表账户屏幕，显示层次结构至第 3 级：

`hledger-ui --bs --tree --depth 3`

- 进入该账户的屏幕，显示已清除的交易，并在记账文件更改时重新加载：

`hledger-ui --register {{assets:bank:checking}} --cleared --watch`

- 读取两个记账文件，并在已知时显示金额的当前值：

`hledger-ui --file {{path/to/2024.journal}} --file {{path/to/2024-prices.journal}} --value now`

- 如果可能，以 Info 格式显示手册：

`hledger-ui --info`

- 显示帮助：

`hledger-ui --help`
