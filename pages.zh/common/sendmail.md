# sendmail

> 发送电子邮件。
> 更多信息：<https://manned.org/sendmail>。

- 将 `message.txt` 的内容发送到本地用户 `username` 的邮件目录：

`sendmail {{username}} < {{message.txt}}`

- 从 you@yourdomain.com（假设邮件服务器已为此配置）发送电子邮件到 test@gmail.com，内容为 `message.txt` 中的信息：

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}`

- 从 you@yourdomain.com（假设邮件服务器已为此配置）发送电子邮件到 test@gmail.com，内容为文件 `file.zip`：

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}`