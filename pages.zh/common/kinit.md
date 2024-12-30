# kinit

> 使用 Kerberos 服务器对主体进行身份验证，以获取并缓存票证。
> 注意：Kerberos 主体可以是用户、服务或应用程序。
> 更多信息：<https://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html>。

- 认证用户并获取票据授权票证：

`kinit {{用户名}}`

- 续订票据授权票证：

`kinit -R`

- 为票证指定有效期：

`kinit -l {{5h}}`

- 为票证指定总可续订有效期：

`kinit -r {{1w}}`

- 指定不同的主体名称进行身份验证：

`kinit -p {{主体@领域}}`

- 指定不同的密钥表文件进行身份验证：

`kinit -t {{路径/到/密钥表}}`