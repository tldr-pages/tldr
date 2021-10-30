# ac

> 打印用户连接时长数据。
> 更多信息：<https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- 以小时为单位打印当前用户连接时间：

`ac`

- 以小时为单位打印所有用户连接时间：

`ac --individual-totals`

- 以小时为单位打印特定用户连接时间：

`ac --individual-totals {{用户名}}`

- 以小时为单位打印特定用户每天连接时间：

`ac --daily-totals --individual-totals {{用户名}}`

- 显示附加明细：

`ac --compatibility`
