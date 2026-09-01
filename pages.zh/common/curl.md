# curl

> 从服务器接收数据或者向服务器发送数据。
> 支持包括 HTTP、HTTPS、FTP 和 SCP 在内的大多数协议。
> 另请参阅：`wcurl`, `wget`。
> 更多信息：<https://curl.se/docs/manpage.html>。

- 发起 HTTP GET 请求，将响应内容输出到 `stdout`：

`curl {{https://example.com}}`

- 发起 HTTP GET 请求，自动跟随所有 `3xx` 重定向，将响应头和内容输出到 `stdout`：

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- 按照 URL 指定的文件名保存下载内容：

`curl {{[-O|--remote-name]}} {{https://example.com/filename.zip}}`

- 以表单编码格式发送数据（`application/x-www-form-urlencoded` 类型的 POST 请求）。如需从 `stdin` 读取数据，可使用 `--data @file_name` 或 `--data @'-'`：

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{name=bob}}' {{http://example.com/form}}`

- 通过代理（如 BurpSuite）使用自定义 HTTP 方法发送带有额外请求头的请求，同时忽略不安全的自签名证书：

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- 设置正确的 `Content-Type` 请求头，以 JSON 格式发送数据：

`curl {{[-d|--data]}} '{{{"name":"bob"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/users/1234}}`

- 跳过证书验证，使用客户端证书和私钥发起请求：

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- 将主机名解析为自定义 IP 地址，以详细模式输出结果（类似于通过编辑 `/etc/hosts` 文件自定义 DNS 解析）：

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
