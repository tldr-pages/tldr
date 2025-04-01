# kinit

> 使用 Kerberos 服务器验证主体以获取并缓存票据。
> 注意：Kerberos 主体可以是用户、服务或应用程序。
> 更多信息：<https://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html>。

- 验证用户并获取票据授予票据：

`kinit {{username}}`

- 刷新票据授予票据：

`kinit -R`

- 指定票据的有效期：

`kinit -l {{5h}}`

- 指定票据的总可刷新有效期：

`kinit -r {{1w}}`

- 指定不同的主体名称进行验证：

`kinit -p {{principal@REALM}}`

- 指定不同的密钥表文件进行验证：

`kinit -t {{path/to/keytab}}`
