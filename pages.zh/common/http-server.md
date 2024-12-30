# http-server

> 简单的静态 HTTP 服务器，用于提供静态文件。
> 更多信息：<https://github.com/http-party/http-server>。

- 启动一个在默认端口上监听的 HTTP 服务器，以提供当前目录：

`http-server`

- 在特定端口上启动一个 HTTP 服务器，以提供特定目录：

`http-server {{path/to/directory}} --port {{port}}`

- 使用基本认证启动一个 HTTP 服务器：

`http-server --username {{username}} --password {{password}}`

- 启动一个禁用目录列表的 HTTP 服务器：

`http-server -d {{false}}`

- 使用指定证书在默认端口上启动一个 HTTPS 服务器：

`http-server --ssl --cert {{path/to/cert.pem}} --key {{path/to/key.pem}}`

- 启动一个 HTTP 服务器，并在输出日志中包含客户端的 IP 地址：

`http-server --log-ip`

- 启动一个启用 CORS 的 HTTP 服务器，在所有响应中包含 `Access-Control-Allow-Origin: *` 头：

`http-server --cors`

- 启动一个禁用日志记录的 HTTP 服务器：

`http-server --silent`