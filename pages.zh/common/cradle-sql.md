# cradle sql

> 管理 Cradle SQL 数据库。
> 更多信息：<https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>。

- 重建数据库模式：

`cradle sql build`

- 为特定包重建数据库模式：

`cradle sql build {{package}}`

- 清空整个数据库：

`cradle sql flush`

- 清空特定包的数据库表：

`cradle sql flush {{package}}`

- 为所有包填充表数据：

`cradle sql populate`

- 为特定包填充表数据：

`cradle sql populate {{package}}`