# calibre-server

> 一个用于在网络中分发电子书的服务器应用程序。
> 注意：电子书必须已经通过图形界面或 `calibredb` 命令行工具导入到图书馆中。
> Calibre 电子书库的一部分。
> 更多信息：<https://manual.calibre-ebook.com/generated/en/calibre-server.html>。

- 启动分发电子书的服务器。访问地址：<http://localhost:8080>:

`calibre-server`

- 在不同的端口启动服务器。访问地址：<http://localhost:port>:

`calibre-server --port {{port}}`

- 为服务器设置密码保护:

`calibre-server --username {{username}} --password {{password}}`