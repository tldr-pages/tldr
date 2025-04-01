# msmtp

> SMTP 客户端。
> 它从 `stdin` 读取文本并将其发送到 SMTP 服务器。
> 更多信息：<https://marlam.de/msmtp>。

- 使用 `~/.msmtprc` 中配置的默认账户发送电子邮件：

`echo "{{Hello world}}" | msmtp {{to@example.org}}`

- 使用 `~/.msmtprc` 中配置的特定账户发送电子邮件：

`echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}`

- 不使用配置的账户发送电子邮件。密码应在 `~/.msmtprc` 文件中指定：

`echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`