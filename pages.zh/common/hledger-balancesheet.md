# hledger 资产负债表

> 显示资产和负债账户的期末余额。
> 金额以正常的正数形式显示，类似于传统的财务报表。
> 更多信息：<https://hledger.org/hledger.html#balancesheet>。

- 显示 `资产` 和 `负债` 账户的当前余额，排除零余额：

`hledger balancesheet`

- 仅显示流动资产（`现金` 账户类型）：

`hledger balancesheet type:C`

- 包括零余额的账户，并显示账户层级：

`hledger balancesheet --empty --tree`

- 显示每个月的余额：

`hledger balancesheet --monthly`

- 显示每个月期末的余额市场价值，以本国货币表示：

`hledger balancesheet --monthly -V`

- 显示季度余额，仅显示账户层级的前两级：

`hledger balancesheet --quarterly --tree --depth 2`

- 上述命令的简短形式，并在 `bs.html` 中生成 HTML 输出：

`hledger bs -Qt -2 -o bs.html`