# hledger print

> 显示完整的日记条目，表示交易。
> 更多信息：<https://hledger.org/hledger.html#print>。

- 显示默认日记文件中的所有交易：

`hledger print`

- 显示交易，使隐含的金额或成本明确化：

`hledger print --explicit --infer-costs`

- 从两个指定文件中显示交易，并将金额转换为成本：

`hledger print --file {{path/to/2023.journal}} --file {{path/to/2024.journal}} --cost`

- 显示本月在 `*food*` 但不在 `*groceries*` 账户中的 `$` 交易：

`hledger print cur:\\$ food not:groceries date:thismonth`

- 显示金额为 50 或以上的，描述中包含 `whole foods` 的交易：

`hledger print amt:'>50' desc:'whole foods'`

- 显示已清账的交易，四舍五入 `EUR` 金额，并使用小数逗号：

`hledger print --cleared --commodity '1000, EUR' --round hard`

- 将 `foo.journal` 中的交易写入 CSV 文件：

`hledger print --file {{path/to/foo.journal}} --output-file {{path/to/output_file.csv}}`