# xh

> 发送 HTTP 请求的友好且快速的工具。
> 注意：`xh` 用 Rust 编写，可以作为 `http` 的有效替代工具。
> 参见：`http`，`curl`。
> 更多信息：<https://github.com/ducaale/xh>。

- 发送 GET 请求：

`xh {{httpbin.org/get}}`

- 发送带有 JSON 正文的 POST 请求（键值对将添加到顶层 JSON 对象中 - 例如：`{"name": "john", "age": 25}`）：

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- 发送带有查询参数的 GET 请求（例如：`first_param=5&second_param=true`）：

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- 发送带有自定义头部信息的 GET 请求：

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- 发送 GET 请求并将响应体保存到文件中：

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`

- 显示等效的 `curl` 命令（这不会发送任何请求）：

`xh --{{curl|curl-long}} {{--follow --verbose get http://example.com user-agent:curl}}`