# neomutt

> NeoMutt 命令行电子邮件客户端。
> 更多信息：<https://neomutt.org>。

- 打开指定的邮件箱：

`neomutt -f {{path/to/mailbox}}`

- 开始撰写邮件，并指定主题和抄送收件人：

`neomutt -s "{{subject}}" -c {{cc@example.com}} {{recipient@example.com}}`

- 发送带有附件的邮件：

`neomutt -a {{path/to/file1 path/to/file2 ...}} -- {{recipient@example.com}}`

- 指定一个文件作为邮件正文：

`neomutt -i {{path/to/file}} {{recipient@example.com}}`

- 指定一个包含邮件头部和正文的草稿文件，格式为 RFC 5322：

`neomutt -H {{path/to/file}} {{recipient@example.com}}`