# updog

> Python的SimpleHTTPServer的替代品。
> 它允许通过HTTP/S进行上传和下载，可以设置临时SSL证书并使用HTTP基本身份验证。
> 更多信息：<https://github.com/sc0tfree/updog>。

- 为当前目录启动HTTP服务器：

`updog`

- 为指定目录启动HTTP服务器：

`updog --directory {{/path/to/directory}}`

- 在指定端口启动HTTP服务器：

`updog --port {{port}}`

- 以密码启动HTTP服务器（登录时，用户名留空，在密码字段中输入密码）：

`updog --password {{password}}`

- 通过SSL启用传输加密：

`updog --ssl`