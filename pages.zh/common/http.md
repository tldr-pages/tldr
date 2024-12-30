# http

> HTTPie：一个旨在测试、调试和与API及HTTP服务器进行交互的HTTP客户端。
> 更多信息：<https://httpie.io/docs/cli/usage>。

- 进行一个简单的GET请求（显示响应头和内容）：

`http {{https://example.com}}`

- 打印内容的特定部分（`H`：请求头，`B`：请求体，`h`：响应头，`b`：响应体，`m`：响应元数据）：

`http --print {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- 在发送请求时指定HTTP方法，并使用代理来拦截请求：

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- 跟随任何`3xx`重定向，并在请求中指定额外的头信息：

`http {{-F|--follow}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- 使用不同的认证方法向服务器进行身份验证：

`http --auth {{username:password|token}} --auth-type {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- 构造请求但不发送（类似于试运行）：

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- 使用命名会话进行持久化自定义头信息、认证凭证和Cookies：

`http --session {{session_name|path/to/session.json}} {{--auth username:password https://example.com/auth API-KEY:xxx}}`

- 将文件上传到表单（下面的示例假设表单字段为`<input type="file" name="cv" />`）：

`http --form {{POST}} {{https://example.com/upload}} {{cv@path/to/file}}`