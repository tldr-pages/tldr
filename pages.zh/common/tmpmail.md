# tmpmail

> 一个直接在终端中使用的临时邮箱，用 POSIX sh 编写。
> 更多信息：<https://github.com/sdushantha/tmpmail>。

- 创建一个临时收件箱：

`tmpmail --generate`

- 列出邮件及其数字ID：

`tmpmail`

- 显示最近收到的邮件：

`tmpmail --recent`

- 打开特定的邮件：

`tmpmail {{email_id}}`

- 查看邮件的纯文本内容，不包含 HTML 标签：

`tmpmail --text`

- 使用特定的浏览器打开邮件（默认浏览器是 w3m）：

`tmpmail --browser {{browser}}`
