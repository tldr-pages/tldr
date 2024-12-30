# serve

> 静态文件服务和目录列表。
> 更多信息：<https://github.com/vercel/serve>。

- 启动一个HTTP服务器，监听默认端口以服务当前目录：

`serve`

- 在特定的[p]ort上启动一个HTTP服务器以服务特定目录：

`serve -p {{port}} {{path/to/directory}}`

- 启动一个HTTP服务器，通过在所有响应中包含`Access-Control-Allow-Origin: *`头来启用CORS：

`serve --cors`

- 在默认端口启动一个HTTP服务器，将所有未找到的请求重写为`index.html`文件：

`serve --single`

- 使用指定的证书在默认端口启动一个HTTPS服务器：

`serve --ssl-cert {{path/to/cert.pem}} --ssl-key {{path/to/key.pem}}`

- 在默认端口上使用特定配置文件启动一个HTTP服务器：

`serve --config {{path/to/serve.json}}`

- 显示帮助信息：

`serve --help`