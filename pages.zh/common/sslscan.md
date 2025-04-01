# sslscan

> 检查服务器支持的 SSL/TLS 协议和加密套件。
> 更多信息：<https://github.com/rbsec/sslscan>。

- 测试端口 443 上的服务器：

`sslscan {{example.com}}`

- 测试指定的端口：

`sslscan {{example.com}}:{{465}}`

- 显示证书信息：

`testssl --show-certificate {{example.com}}`
