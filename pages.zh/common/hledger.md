# hledger

> 一个强大且友好的纯文本会计应用程序。
> 还有：`hledger-ui` 用于 TUI，`hledger-web` 用于 Web 界面。
> 更多信息：<https://hledger.org/hledger.html>。

- 交互式记录新交易，保存到默认的记账文件：

`hledger add`

- 从 `bank.csv` 导入新交易，使用 `bank.csv.rules` 进行转换：

`hledger import {{path/to/bank.csv}}`

- 打印所有交易，从多个指定的记账文件中读取：

`hledger print --file {{path/to/prices-2024.journal}} --file {{path/to/prices-2023.journal}}`

- 以层次结构显示所有账户及其类型：

`hledger accounts --tree --types`

- 以层次结构显示资产和负债账户余额，包括余额为零的账户：

`hledger balancesheet --empty --tree --no-elide`

- 显示每月的收入/支出/总计，按最大数值排序，汇总到 2 级：

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- 显示 `assets:bank:checking` 账户的交易和当前余额：

`hledger aregister assets:bank:checking`

- 显示从 `assets:cash` 账户中花费在食物上的金额：

`hledger print assets:cash | hledger -f- -I aregister expenses:food`