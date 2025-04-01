# curlie

> 一个 `curl` 的前端工具，增加了 `httpie` 的易用性。
> 更多信息：<https://github.com/rs/curlie>.

- 发送 GET 请求：

`curlie {{httpbin.org/get}}`

- 发送 POST 请求：

`curlie post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- 发送带有查询参数的 GET 请求（例如 `first_param=5&second_param=true`）：

`curlie get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- 发送带有自定义头部的 GET 请求：

`curlie get {{httpbin.org/get}} {{header-name:header-value}}`