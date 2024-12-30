# ac

> 打印用户连接时长的统计信息。
> 更多信息：<https://www.gnu.org/software/acct/manual/accounting.html#ac>。

- 打印当前用户连接的时长（以小时为单位）：

`ac`

- 打印所有用户连接的时长（以小时为单位）：

`ac --individual-totals`

- 打印特定用户连接的时长（以小时为单位）：

`ac --individual-totals {{username}}`

- 打印特定用户每天连接的时长（包括总计）：

`ac --daily-totals --individual-totals {{username}}`

- 还显示附加细节：

`ac --compatibility`