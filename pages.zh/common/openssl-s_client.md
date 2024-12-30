# openssl s_client

> 用于创建TLS客户端连接的OpenSSL命令。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>。

- 显示域证书的开始和到期日期：

`openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates`

- 显示SSL/TLS服务器呈现的证书：

`openssl s_client -connect {{host}}:{{port}} </dev/null`

- 在连接SSL/TLS服务器时设置服务器名称指示符（SNI）：

`openssl s_client -connect {{host}}:{{port}} -servername {{hostname}}`

- 显示HTTPS服务器的完整证书链：

`openssl s_client -connect {{host}}:443 -showcerts </dev/null`