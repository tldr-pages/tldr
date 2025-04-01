# openssl s_client

> OpenSSL 命令用于创建 TLS 客户端连接。
> 更多信息：<https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- 显示域名证书的开始和过期日期：

`openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates`

- 显示 SSL/TLS 服务器提供的证书：

`openssl s_client -connect {{host}}:{{port}} </dev/null`

- 连接 SSL/TLS 服务器时设置服务器名称指示 (SNI)：

`openssl s_client -connect {{host}}:{{port}} -servername {{hostname}}`

- 显示 HTTPS 服务器的完整证书链：

`openssl s_client -connect {{host}}:443 -showcerts </dev/null>`
