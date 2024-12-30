# calibre-server

> 一款用于通过网络分发电子书的服务器应用程序。
> 注意：电子书必须已经通过GUI或`calibredb`命令行导入到库中。
> 这是Calibre电子书库的一部分。
> 更多信息请访问：<https://manual.calibre-ebook.com/generated/en/calibre-server.html>。

- 启动一个服务器以分发电子书。访问地址为<http://localhost:8080>：

`calibre-server`

- 在不同的端口上启动服务器。访问地址为<http://localhost:port>：

`calibre-server --port {{port}}`

- 保护服务器密码：

`calibre-server --username {{username}} --password {{password}}`