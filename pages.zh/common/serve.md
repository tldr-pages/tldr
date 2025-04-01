# serve

> 静态文件服务和目录列表。
> 更多信息：<https://github.com/vercel/serve>。

- 启动一个监听默认端口以服务当前目录的 HTTP 服务器：

`serve`

- 启动一个监听特定 [p]ort 端口以服务特定目录的 HTTP 服务器：

`serve -p {{port}} {{path/to/directory}}`

- 启动一个启用 CORS 的 HTTP 服务器，通过在所有响应中包含 `Access-Control-Allow-Origin: *` 标头：

`serve --cors`

- 启动一个默认端口的 HTTP 服务器，将所有未找到的请求重写到 `index.html` 文件：

`serve --single`

- 启动一个使用指定证书的默认端口的 HTTPS 服务器：

`serve --ssl-cert {{path/to/cert.pem}} --ssl-key {{path/to/key.pem}}`

- 启动一个使用特定配置文件的默认端口的 HTTP 服务器：

`serve --config {{path/to/serve.json}}`

- 显示帮助：

`serve --help`
