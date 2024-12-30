# mailx

> 发送和接收邮件。
> 更多信息：<https://manned.org/mailx>。

- 发送邮件（内容应在命令后输入，并以 `Ctrl+D` 结束）：

`mailx -s "{{subject}}" {{to_addr}}`

- 通过另一个命令传递内容发送邮件：

`echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}`

- 从文件中读取内容发送邮件：

`mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}`

- 发送邮件给一个收件人并抄送到另一个地址：

`mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}`

- 发送邮件时指定发件人地址：

`mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}`

- 发送带有附件的邮件：

`mailx -a {{path/to/file}} -s "{{subject}}" {{to_addr}}`