# hledger incomestatement

> 显示报告期间的收入流入和支出流出。
> 金额以常规正号显示，如同传统的财务报表。
> 更多信息：<https://hledger.org/hledger.html#incomestatement>。

- 显示收入和支出（`Revenue` 和 `Expense` 账户的变化）：

`hledger incomestatement`

- 按月显示收入和支出：

`hledger incomestatement --monthly`

- 按月显示收入/支出/总计，按大小排序，汇总到 2 级：

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- 上述命令的简写形式，并生成 `is.html` 文件的 HTML 输出：

`hledger is -MTAS -2 -o is.html`