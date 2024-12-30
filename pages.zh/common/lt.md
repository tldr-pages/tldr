# lt

> Localtunnel 将您的本地主机暴露给全世界，以便于测试和共享。
> 更多信息：<https://github.com/localtunnel/localtunnel>。

- 从特定端口启动隧道：

`lt --port {{8000}}`

- 指定进行转发的上游服务器：

`lt --port {{8000}} --host {{host}}`

- 请求特定的子域名：

`lt --port {{8000}} --subdomain {{subdomain}}`

- 打印基本请求信息：

`lt --port {{8000}} --print-requests`

- 在默认网页浏览器中打开隧道 URL：

`lt --port {{8000}} --open`