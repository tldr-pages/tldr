# xh

> 友好且快速的HTTP请求发送工具。
> 注意：`xh` 是用Rust编写的，有效地替代了 `http`。
> 另请参阅：`http`，`curl`。
> 更多信息：<https://github.com/ducaale/xh>。

- 发送GET请求：

`xh {{httpbin.org/get}}`

- 发送带有JSON主体的POST请求（键值对将添加到顶级JSON对象中 - 例如 `{"name": "john", "age": 25}`）：

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- 发送带有查询参数的GET请求（例如 `first_param=5&second_param=true`）：

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- 发送带有自定义头部的GET请求：

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- 发起GET请求并将响应主体保存到文件中：

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`

- 显示等效的 `curl` 命令（这不会发送任何请求）：

`xh --{{curl|curl-long}} {{--follow --verbose get http://example.com user-agent:curl}}`