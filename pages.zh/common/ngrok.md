# ngrok

> 反向代理，创建从公网端点到本地运行的Web服务的加密隧道。
> 更多信息：<https://ngrok.com>.

- 暴露指定端口上的本地HTTP服务：

`ngrok http {{80}}`

- 暴露指定主机上的本地HTTP服务：

`ngrok http {{foo.dev}}:{{80}}`

- 暴露本地HTTPS服务器：

`ngrok http https://localhost`

- 暴露指定端口上的TCP流量：

`ngrok tcp {{22}}`

- 为指定主机和端口暴露TLS流量：

`ngrok tls -hostname={{foo.com}} {{443}}`
