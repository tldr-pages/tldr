# ngrok

> 反向代理，通过公共端点创建一个安全隧道，连接到本地运行的web服务。
> 更多信息：<https://ngrok.com>。

- 在指定端口上暴露本地HTTP服务：

`ngrok http {{80}}`

- 在特定主机上暴露本地HTTP服务：

`ngrok http {{foo.dev}}:{{80}}`

- 暴露本地HTTPS服务器：

`ngrok http https://localhost`

- 在指定端口上暴露TCP流量：

`ngrok tcp {{22}}`

- 为特定主机和端口暴露TLS流量：

`ngrok tls -hostname={{foo.com}} {{443}}`