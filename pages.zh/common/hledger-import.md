# hledger 导入

> 从一个或多个数据文件导入新交易到主日记账。
> 更多信息：<https://hledger.org/hledger.html#import>。

- 从 `bank.csv` 导入新交易，使用 `bank.csv.rules` 进行转换：

`hledger import {{path/to/bank.csv}}`

- 显示从这两个文件将要导入的内容，而不执行任何操作：

`hledger import {{path/to/bank1.csv}} {{path/to/bank2.csv}} --dry-run`

- 从所有 CSV 文件导入新交易，使用相同的规则：

`hledger import --rules-file {{common.rules}} *.csv`

- 在编辑 `bank.csv.rules` 时显示转换错误或结果：

`watchexec -- hledger -f {{path/to/bank.csv}} print`

- 标记 `bank.csv` 的当前数据为已查看，仿佛已经导入：

`hledger import --catchup {{path/to/bank.csv}}`

- 标记 `bank.csv` 为全新，仿佛尚未导入：

`rm -f .latest.bank.csv`