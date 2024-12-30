# 账本

> 一个强大的复式记账系统。
> 更多信息：<https://www.ledger-cli.org>。

- 打印显示总额的余额报告：

`ledger balance --file {{path/to/ledger.journal}}`

- 列出所有按金额排序的费用记录：

`ledger register {{expenses}} --sorted {{amount}}`

- 打印除饮料和食物外的总费用：

`ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})`

- 打印预算报告：

`ledger budget`

- 打印所有记录的汇总信息：

`ledger stats`