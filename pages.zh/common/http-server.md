# http-server

> 简单的静态 HTTP 服务器，用于提供静态文件。
> 更多信息：<https://github.com/http-party/http-server>.

- 在默认端口启动 HTTP 服务器，提供当前目录的内容：

`http-server`

- 在特定端口启动 HTTP 服务器，提供特定目录的内容：

`http-server {{path/to/directory}} --port {{port}}`

- 使用基本认证启动 HTTP 服务器：

`http-server --username {{username}} --password {{password}}`

- 禁用目录列表启动 HTTP 服务器：

`http-server -d {{false}}`

- 使用指定的证书在默认端口启动 HTTPS 服务器：

`http-server --ssl --cert {{path/to/cert.pem}} --key {{path/to/key.pem}}`

- 启动 HTTP 服务器并将客户端的 IP 地址包含在输出日志中：

`http-server --log-ip`

- 启动带有 CORS 支持的 HTTP 服务器，通过在所有响应中添加 `Access-Control-Allow-Origin: *` 头：

`http-server --cors`

- 禁用日志记录启动 HTTP 服务器：

`http-server --silent`
