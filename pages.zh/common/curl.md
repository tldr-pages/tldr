# curl

> 向 / 从一个服务器传输数据。
> 支持大多数协议，包括 HTTP, FTP, 和 POP3.
> 更多信息：<https://curl.se>.

- 将指定 URL 的内容下载到文件：

`curl {{http://example.com}} --output {{文件名}}`

- 将文件从 URL 保存到由 URL 指示的文件名中：

`curl --remote-name {{http://example.com/filename}}`

- 下载文件，跟随 重定向，并且自动 续传（恢复）前序文件传输：

`curl --remote-name --location --continue-at - {{http://example.com/filename}}`

- 发送表单编码数据（`application/x-www-form-urlencoded` 的 POST 请求）：

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- 发送带有额外请求头，使用自定义请求方法的请求：

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- 发送 JSON 格式的数据，并附加正确的 `Content-Type` 请求头：

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- 使用用户名和密码，授权访问服务器：

`curl --user myusername:mypassword {{http://example.com}}`

- 为指定资源使用客户端证书和密钥，并且跳过证书验证：

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
