# hledger 打印

> 显示完整的日记条目，代表交易。
> 更多信息：<https://hledger.org/hledger.html#print>。

- 显示默认日记文件中的所有交易：

`hledger print`

- 显示交易，任何隐含的金额或成本显式化：

`hledger print --explicit --infer-costs`

- 显示来自两个指定文件的交易，金额转换为成本：

`hledger print --file {{path/to/2023.journal}} --file {{path/to/2024.journal}} --cost`

- 显示本月在`*food*`但不在`*groceries*`账户中的`$`交易：

`hledger print cur:\\$ food not:groceries date:thismonth`

- 显示金额为50或更多的交易，其描述中包含`whole foods`：

`hledger print amt:'>50' desc:'whole foods'`

- 显示已清除的交易，`EUR`金额取整并使用小数逗号：

`hledger print --cleared --commodity '1000, EUR' --round hard`

- 将`foo.journal`中的交易写入CSV文件：

`hledger print --file {{path/to/foo.journal}} --output-file {{path/to/output_file.csv}}`