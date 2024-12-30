# live-server

> 一个简单的开发 HTTP 服务器，具有实时重载功能。
> 更多信息：<https://github.com/tapio/live-server>。

- 提供一个 `index.html` 文件，并在更改时重新加载：

`live-server`

- 指定一个端口（默认是 8080）来提供文件：

`live-server --port={{8081}}`

- 指定要提供的特定文件：

`live-server --open={{about.html}}`

- 将所有对 ROUTE 的请求代理到 URL：

`live-server --proxy={{/}}:{{http:localhost:3000}}`