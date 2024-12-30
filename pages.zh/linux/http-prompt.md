# http-prompt

> 一个交互式命令行HTTP客户端，具有自动补全和语法高亮功能。
> 更多信息：<https://github.com/httpie/http-prompt>。

- 启动一个会话，目标为默认URL <http://localhost:8000> 或上一个会话：

`http-prompt`

- 启动一个会话，指定给定的URL：

`http-prompt {{http://example.com}}`

- 启动一个会话，并带有一些初始选项：

`http-prompt {{localhost:8000/api}} --auth {{username:password}}`