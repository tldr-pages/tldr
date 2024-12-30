# curl

> 从服务器传输数据。
> 支持大多数协议，包括 HTTP、HTTPS、FTP、SCP 等。
> 更多信息：<https://curl.se/docs/manpage.html>。

- 发起一个 HTTP GET 请求，并将内容输出到 `stdout`：

`curl {{https://example.com}}`

- 发起一个 HTTP GET 请求，跟随任何 `3xx` 重定向，并将回复的头部和内容输出到 `stdout`：

`curl --location --dump-header - {{https://example.com}}`

- 下载文件，将输出保存为 URL 指定的文件名：

`curl --remote-name {{https://example.com/filename.zip}}`

- 发送表单编码的数据（`application/x-www-form-urlencoded` 类型的 POST 请求）。使用 `--data @file_name` 或 `--data @'-'` 从 `stdin` 读取：

`curl -X POST --data {{'name=bob'}} {{http://example.com/form}}`

- 使用额外的头部、定制的 HTTP 方法并通过代理（如 BurpSuite）发送请求，忽略不安全的自签名证书：

`curl -k --proxy {{http://127.0.0.1:8080}} --header {{'Authorization: Bearer token'}} --request {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- 以 JSON 格式发送数据，指定适当的 Content-Type 头部：

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- 为资源传递客户端证书和密钥，跳过证书验证：

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`

- 将主机名解析为自定义 IP 地址，并输出详细信息（类似于编辑 `/etc/hosts` 文件以实现自定义 DNS 解析）：

`curl --verbose --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`