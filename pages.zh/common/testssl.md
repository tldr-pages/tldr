# testssl

> 检查服务器支持的 SSL/TLS 协议和密码套件。
> 更多信息：<https://testssl.sh/>.

- 在端口 443 上测试服务器（运行所有检查）：

`testssl {{example.com}}`

- 测试不同的端口：

`testssl {{example.com:465}}`

- 仅检查可用的协议：

`testssl --protocols {{example.com}}`

- 仅检查漏洞：

`testssl --vulnerable {{example.com}}`

- 仅检查 HTTP 安全头部：

`testssl --headers {{example.com}}`

- 测试其他启用 STARTTLS 的协议：

`testssl --starttls {{ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql}} {{example.com}}:{{port}}`