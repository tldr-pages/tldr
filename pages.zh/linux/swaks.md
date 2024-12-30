# swaks

> 瑞士军刀SMTP，全功能SMTP事务测试工具。
> 更多信息：<https://github.com/jetmore/swaks/blob/develop/doc/base.pod>。

- 将标准测试电子邮件发送到 `user@example.com`，使用 `test-server.example.net` 的 25 端口：

`swaks --to {{user@example.com}} --server {{test-server.example.net}}`

- 发送一封标准测试电子邮件，要求以用户 `me@example.com` 进行 CRAM-MD5 身份验证。邮件正文将添加一个 "X-Test" 头：

`swaks --to {{user@example.com}} --from {{me@example.com}} --auth {{CRAM-MD5}} --auth-user {{me@example.com}} --header-X-Test "{{test_email}}"`

- 使用 EICAR 作为附件测试病毒扫描器。不要显示消息数据部分：

`swaks -t {{user@example.com}} --attach - --server {{test-server.example.com}} --suppress-data {{path/to/eicar.txt}}`

- 使用 GTUBE 在电子邮件正文中测试垃圾邮件扫描器，通过 `example.com` 的 MX 记录路由：

`swaks --to {{user@example.com}} --body {{path/to/gtube_file}}`

- 通过 UNIX 域套接字文件使用 LMTP 协议将标准测试电子邮件发送到 `user@example.com`：

`swaks --to {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`