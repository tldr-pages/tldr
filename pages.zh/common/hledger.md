# hledger

> 一个强大、友好的纯文本会计应用程序。
> 另请参见：`hledger-ui` 用于 TUI，`hledger-web` 用于网络界面。
> 更多信息：<https://hledger.org/hledger.html>。

- 交互式记录新交易，并保存到默认日记文件：

`hledger add`

- 从 `bank.csv` 导入新交易，使用 `bank.csv.rules` 进行转换：

`hledger import {{path/to/bank.csv}}`

- 打印所有交易，从多个指定的日记文件读取：

`hledger print --file {{path/to/prices-2024.journal}} --file {{path/to/prices-2023.journal}}`

- 显示所有账户，作为层级结构及其类型：

`hledger accounts --tree --types`

- 显示资产和负债账户余额，包括零，层级显示：

`hledger balancesheet --empty --tree --no-elide`

- 显示每月的收入/支出/总额，按从大到小排序，汇总到 2 层级：

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- 显示 `assets:bank:checking` 账户的交易和余额：

`hledger aregister assets:bank:checking`

- 显示从 `assets:cash` 账户上消费的食品金额：

`hledger print assets:cash | hledger -f- -I aregister expenses:food`