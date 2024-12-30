# hledger-ui

> `hledger` 的终端界面（TUI），这是一个强大、友好的纯文本会计应用程序。
> 更多信息请访问: <https://hledger.org/hledger-ui.html>。

- 从默认的日记文件启动主菜单屏幕：

`hledger-ui`

- 使用不同的颜色主题启动：

`hledger-ui --theme {{terminal|greenterm|dark}}`

- 在资产负债表账户屏幕启动，显示到第三级的层级：

`hledger-ui --bs --tree --depth 3`

- 在此账户的屏幕上启动，显示已清算的交易，并在更改时重新加载：

`hledger-ui --register {{assets:bank:checking}} --cleared --watch`

- 阅读两个日记文件，并在已知时显示金额的当前值：

`hledger-ui --file {{path/to/2024.journal}} --file {{path/to/2024-prices.journal}} --value now`

- 如果可能，以信息格式显示手册：

`hledger-ui --info`

- 显示帮助信息：

`hledger-ui --help`