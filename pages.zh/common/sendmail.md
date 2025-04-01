# sendmail

> 发送邮件。
> 更多信息：<https://manned.org/sendmail>。

- 将 `message.txt` 的内容发送到本地用户 `username` 的邮件目录中：

`sendmail {{username}} < {{message.txt}}`

- 从 you@yourdomain.com（假设邮件服务器已为此配置）向 test@gmail.com 发送包含 `message.txt` 内容的邮件：

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}`

- 从 you@yourdomain.com（假设邮件服务器已为此配置）向 test@gmail.com 发送包含 `file.zip` 的邮件：

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}`
