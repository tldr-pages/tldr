# lt

> Localtunnel（本地隧道）将您的本地主机暴露给世界，便于测试和分享。
> 更多信息：<https://github.com/localtunnel/localtunnel>.

- 从指定端口启动隧道：

`lt --port {{8000}}`

- 指定执行转发的上游服务器：

`lt --port {{8000}} --host {{host}}`

- 请求特定的子域名：

`lt --port {{8000}} --subdomain {{subdomain}}`

- 打印基本请求信息：

`lt --port {{8000}} --print-requests`

- 在默认的网络浏览器中打开隧道URL：

`lt --port {{8000}} --open`
