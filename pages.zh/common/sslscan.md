# sslscan

> 检查服务器支持的SSL/TLS协议和密码套件。
> 更多信息：<https://github.com/rbsec/sslscan>。

- 测试443端口的服务器：

`sslscan {{example.com}}`

- 测试指定端口：

`sslscan {{example.com}}:{{465}}`

- 显示证书信息：

`testssl --show-certificate {{example.com}}`