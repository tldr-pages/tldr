# http

> HTTPie: 用于测试、调试和与 API 及 HTTP 服务器交互的 HTTP 客户端。
> 更多信息：<https://httpie.io/docs/cli/usage>.

- 发送简单的 GET 请求（显示响应头和内容）：

`http {{https://example.com}}`

- 打印内容的特定部分（`H`: 请求头, `B`: 请求体, `h`: 响应头, `b`: 响应体, `m`: 响应元数据）：

`http {{[-p|--print]}} {{H|B|h|b|m|Hh|Hhb|...}} {{https://example.com}}`

- 指定发送请求时的 HTTP 方法，并使用代理拦截请求：

`http {{GET|POST|HEAD|PUT|PATCH|DELETE|...}} --proxy {{http|https}}:{{http://localhost:8080|socks5://localhost:9050|...}} {{https://example.com}}`

- 跟随 `3xx` 重定向，并在请求中指定额外的头部信息：

`http {{[-F|--follow]}} {{https://example.com}} {{'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'}}`

- 使用不同的认证方法向服务器认证：

`http {{[-a|--auth]}} {{username:password|token}} {{[-A|--auth-type]}} {{basic|digest|bearer}} {{GET|POST|...}} {{https://example.com/auth}}`

- 构造请求但不发送（类似于干运行）：

`http --offline {{GET|DELETE|...}} {{https://example.com}}`

- 使用命名会话以持久化自定义头部、认证凭证和 cookie：

`http --session {{session_name|path/to/session.json}} {{[-a|--auth]}} {{username}}:{{password}} {{https://example.com/auth}} {{API-KEY:xxx}}`

- 上传文件到表单（以下示例假设表单字段为 `<input type="file" name="cv" />`）：

`http {{[-f|--form]}} {{POST}} {{https://example.com/upload}} {{cv@path/to/file}}`