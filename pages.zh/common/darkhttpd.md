# darkhttpd

> Darkhttpd网页服务器。
> 更多信息：<https://unix4lyfe.org/darkhttpd>。

- 启动服务器，提供指定的文档根目录：

`darkhttpd {{path/to/docroot}}`

- 在指定端口上启动服务器（如果以非root用户身份运行，默认端口为8080）：

`darkhttpd {{path/to/docroot}} --port {{port}}`

- 仅在指定的IP地址上监听（默认情况下，服务器在所有接口上监听）：

`darkhttpd {{path/to/docroot}} --addr {{ip_address}}`