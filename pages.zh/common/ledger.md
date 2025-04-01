# ledger

> 一个强大、复式的会计系统。
> 更多信息：<https://www.ledger-cli.org>。

- 打印显示总额的余额报告：

`ledger balance --file {{path/to/ledger.journal}}`

- 按金额排序列出所有费用明细：

`ledger register {{expenses}} --sorted {{amount}}`

- 打印除饮料和食品外的所有费用总额：

`ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})`

- 打印预算报告：

`ledger budget`

- 打印所有明细的摘要信息：

`ledger stats`
