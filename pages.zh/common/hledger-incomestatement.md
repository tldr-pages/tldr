# hledger 收入报表

> 显示报告期间的收入流入和支出流出。
> 金额以正常的正号显示，如同传统财务报表一样。
> 更多信息：<https://hledger.org/hledger.html#incomestatement>。

- 显示收入和支出（`Revenue` 和 `Expense` 账户的变动）：

`hledger incomestatement`

- 显示每个月的收入和支出：

`hledger incomestatement --monthly`

- 显示每月的收入/支出/总计，按降序排列，汇总到2个级别：

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- 上述命令的简短形式，并生成HTML输出到 `is.html`：

`hledger is -MTAS -2 -o is.html`