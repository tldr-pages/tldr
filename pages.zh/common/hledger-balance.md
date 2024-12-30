# hledger 余额

> 一份灵活的通用“汇总”报告，显示带有某种数字数据的账户。
> 这可以是每个周期的余额变动、期末余额、预算执行情况、未实现的资本收益等。
> 更多信息请访问：<https://hledger.org/hledger.html#balance>。

- 显示所有账户在所有时间段内的所有交易的余额变动：

`hledger balance`

- 以树形结构显示名为 `*expenses*` 的账户的余额变动，仅总结前两级：

`hledger balance {{expenses}} --tree --depth {{2}}`

- 显示每个月的费用及其总额和平均值，按总额排序；以及他们的每月预算目标：

`hledger balance {{expenses}} --monthly --row-total --average --sort-amount --budget`

- 与上述类似，简短形式，通过 `Expense` 类型匹配账户，作为两级树形结构，不压缩无趣的账户：

`hledger bal type:{{X}} -MTAS --budget -t -{{2}} --no-elide`

- 显示 2024 年每个季度的期末余额（包括开始日期之前的交易），在名为 `*assets*` 或 `*liabilities*` 的账户中：

`hledger balance --historical --period '{{quarterly in 2024}}' {{assets}} {{liabilities}}`

- 与上述类似，简短形式；还显示零余额，按总额排序并总结到三层：

`hledger bal -HQ date:{{2024}} type:{{AL}} -ES -{{3}}`

- 显示投资资产在每个季度末的市场价值，以基础货币表示：

`hledger bal -HVQ {{assets:investments}}`

- 显示每个季度非加密货币投资资产因市场价格变动而产生的未实现资本收益/损失：

`hledger bal --gain -Q {{assets:investments}} not:{{cryptocurrency}}`