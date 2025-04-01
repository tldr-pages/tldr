# hledger balance

> 一个灵活的、通用的“汇总”报告，显示带有某种数字数据的账户。
> 这可以是每个时期的余额变化、结束余额、预算执行情况、未实现资本收益等。
> 更多信息：<https://hledger.org/hledger.html#balance>。

- 显示所有账户从所有过账项中所有时间的余额变化：

`hledger balance`

- 显示名为 `*expenses*` 的账户的余额变化，以树形结构形式，仅汇总前两层：

`hledger balance {{expenses}} --tree --depth {{2}}`

- 每月显示费用及其总额和平均值，按总额排序；并显示每月的预算目标：

`hledger balance {{expenses}} --monthly --row-total --average --sort-amount --budget`

- 与上述类似，更简洁的形式，匹配 `Expense` 类型的账户，作为两层树的形式，不压缩枯燥的账户：

`hledger bal type:{{X}} -MTAS --budget -t -{{2}} --no-elide`

- 显示起始日期之前（包括）的余额，2024 年每季度的，名为 `*assets*` 或 `*liabilities*` 的账户的余额：

`hledger balance --historical --period '{{quarterly in 2024}}' {{assets}} {{liabilities}}`

- 与上述类似，更简洁的形式；还显示零余额，按总额排序并汇总到三层：

`hledger bal -HQ date:{{2024}} type:{{AL}} -ES -{{3}}`

- 显示每个季度末投资资产的基本货币市场价值：

`hledger bal -HVQ {{assets:investments}}`

- 显示每个季度因市场价变化而导致的未实现资本收益/损失，适用于非加密货币的投资资产：

`hledger bal --gain -Q {{assets:investments}} not:{{cryptocurrency}}`