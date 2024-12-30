# msmtp

> 一个SMTP客户端。
> 它从`stdin`读取文本并将其发送到SMTP服务器。
> 更多信息请访问：<https://marlam.de/msmtp>。

- 使用在`~/.msmtprc`中配置的默认帐户发送电子邮件：

`echo "{{Hello world}}" | msmtp {{to@example.org}}`

- 使用在`~/.msmtprc`中配置的特定帐户发送电子邮件：

`echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}`

- 在没有配置帐户的情况下发送电子邮件。密码应在`~/.msmtprc`文件中指定：

`echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`