# http-prompt

> 一个具有自动完成和语法高亮功能的交互式命令行 HTTP 客户端。
> 更多信息：<https://github.com/httpie/http-prompt>.

- 启动一个会话，默认目标 URL 为 <http://localhost:8000> 或上次会话：

`http-prompt`

- 启动一个指定 URL 的会话：

`http-prompt {{http://example.com}}`

- 启动一个带有初始选项的会话：

`http-prompt {{localhost:8000/api}} --auth {{username:password}}`
