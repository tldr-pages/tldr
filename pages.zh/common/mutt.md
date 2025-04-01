# mutt

> 命令行电子邮件客户端。
> 更多信息：<http://mutt.org>。

- 打开指定的邮箱：

`mutt -f {{mailbox}}`

- 发送电子邮件并指定主题和抄送收件人：

`mutt -s {{subject}} -c {{cc@example.com}} {{recipient@example.com}}`

- 发送带有附件的电子邮件：

`mutt -a {{file1}} {{file2}} -- {{recipient@example.com}}`

- 指定一个文件作为邮件正文：

`mutt -i {{path/to/file}} {{recipient@example.com}}`

- 指定一个草稿文件，该文件包含消息的头部和正文，格式为 RFC 5322：

`mutt -H {{path/to/file}} {{recipient@example.com}}`
