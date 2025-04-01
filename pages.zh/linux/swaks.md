# swaks

> 瑞士军刀SMTP，多用途SMTP事务测试工具。
> 更多信息：<https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- 向 `test-server.example.net` 的25端口发送一封标准测试邮件到 `user@example.com`：

`swaks --to {{user@example.com}} --server {{test-server.example.net}}`

- 以 `me@example.com` 身份使用 CRAM-MD5 身份验证发送一封标准测试邮件。邮件正文中将添加一个 "X-Test" 标头：

`swaks --to {{user@example.com}} --from {{me@example.com}} --auth {{CRAM-MD5}} --auth-user {{me@example.com}} --header-X-Test "{{test_email}}"`

- 使用 EICAR 附件测试病毒扫描器。不显示邮件数据部分：

`swaks -t {{user@example.com}} --attach - --server {{test-server.example.com}} --suppress-data {{path/to/eicar.txt}}`

- 使用 GTUBE 测试垃圾邮件扫描器，通过 `example.com` 的 MX 记录路由：

`swaks --to {{user@example.com}} --body {{path/to/gtube_file}}`

- 通过 UNIX 域套接字文件使用 LMTP 协议发送一封标准测试邮件到 `user@example.com`：

`swaks --to {{user@example.com}} --socket {{/var/lda.sock}} --protocol {{LMTP}}`