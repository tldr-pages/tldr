# simplehttpserver

> 一个简单的HTTP/S服务器，支持文件上传、基本身份验证以及用于自定义响应的YAML规则。
> Go语言对Python的`http.server`的替代方案。
> 更多信息请访问：<https://github.com/projectdiscovery/simplehttpserver>。

- 启动HTTP服务器，提供当前目录的服务，并输出详细信息（默认在所有接口上监听端口8000）：

`simplehttpserver -verbose`

- 启动HTTP服务器，使用基本身份验证，在所有接口的80端口提供特定路径的服务：

`sudo simplehttpserver -basic-auth {{username}}:{{password}} -path {{/var/www/html}} -listen 0.0.0.0:80`

- 启动HTTP服务器，使用自签名证书启用HTTPS，并在所有接口上自定义SAN：

`sudo simplehttpserver -https -domain {{*.selfsigned.com}} -listen 0.0.0.0:443`

- 启动HTTP服务器，支持自定义响应头和上传功能：

`simplehttpserver -upload -header '{{X-Powered-By: Go}}' -header '{{Server: SimpleHTTPServer}}'`

- 启动HTTP服务器，使用YAML中的自定义规则（请参阅文档以获取DSL）：

`simplehttpserver -rules {{rules.yaml}}`