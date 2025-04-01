# darkhttpd

> Darkhttpd 网络服务器。
> 更多信息：<https://unix4lyfe.org/darkhttpd>。

- 启动服务，指定文档根目录：

`darkhttpd {{path/to/docroot}}`

- 在指定端口启动服务器（默认为8080端口，如果以非root用户运行）：

`darkhttpd {{path/to/docroot}} --port {{port}}`

- 仅监听指定的IP地址（默认情况下，服务器监听所有接口）：

`darkhttpd {{path/to/docroot}} --addr {{ip_address}}`