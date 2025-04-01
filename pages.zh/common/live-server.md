# live-server

> 一个带有实时重载功能的简单开发 HTTP 服务器。
> 更多信息：<https://github.com/tapio/live-server>.

- 服务 `index.html` 文件并在文件更改时自动重载：

`live-server`

- 指定一个端口号（默认为 8080）来服务文件：

`live-server --port={{8081}}`

- 指定要服务的文件：

`live-server --open={{about.html}}`

- 将所有对 ROUTE 的请求代理到 URL：

`live-server --proxy={{/}}:{{http:localhost:3000}}`
