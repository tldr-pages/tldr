# hledger balancesheet

> 显示资产和负债账户的期末余额。
> 金额以正数形式显示，符合传统财务报表的格式。
> 更多信息：<https://hledger.org/hledger.html#balancesheet>。

- 显示 `Asset` 和 `Liability` 账户的当前余额，排除零余额账户：

`hledger balancesheet`

- 仅显示流动资产（`Cash` 账户类型）：

`hledger balancesheet type:C`

- 包含零余额账户，并显示账户层次结构：

`hledger balancesheet --empty --tree`

- 显示每个月末的余额：

`hledger balancesheet --monthly`

- 显示每个月末以本位币计算的市场价值余额：

`hledger balancesheet --monthly -V`

- 显示每季度的余额，并仅显示账户层次结构的前两层：

`hledger balancesheet --quarterly --tree --depth 2`

- 上述命令的简写形式，并生成 `bs.html` 的 HTML 输出：

`hledger bs -Qt -2 -o bs.html`