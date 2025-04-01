# simplehttpserver

> 一个支持文件上传、基本认证和自定义响应的 YAML 规则的简单 HTTP/HTTPS 服务器。
> 是 Python `http.server` 的 Go 语言替代品。
> 更多信息：<https://github.com/projectdiscovery/simplehttpserver>.

- 启动 HTTP 服务器，服务当前目录并输出详细信息（默认监听所有接口和 8000 端口）：

`simplehttpserver -verbose`

- 启动 HTTP 服务器，使用基本认证并服务特定路径，端口 80，监听所有接口：

`sudo simplehttpserver -basic-auth {{username}}:{{password}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- 启动 HTTP 服务器，启用自签名证书的 HTTPS，自定义 SAN，监听所有接口：

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- 启动 HTTP 服务器，启用文件上传并自定义响应头：

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- 启动 HTTP 服务器，使用 YAML 文件中的自定义规则（详见文档中的 DSL）：

`simplehttpserver -rules {{rules.yaml}}`
