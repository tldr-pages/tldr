# tmpmail

> 一个从终端生成的临时邮箱，使用POSIX sh编写。
> 更多信息：<https://github.com/sdushantha/tmpmail>。

- 创建一个临时收件箱：

`tmpmail --generate`

- 列出邮件及其数字ID：

`tmpmail`

- 显示最近收到的邮件：

`tmpmail --recent`

- 打开特定邮件：

`tmpmail {{email_id}}`

- 以原始文本查看邮件，不带HTML标签：

`tmpmail --text`

- 使用特定浏览器打开邮件（默认是w3m）：

`tmpmail --browser {{browser}}`