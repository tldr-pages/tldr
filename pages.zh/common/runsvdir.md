# runsvdir

> 运行整个服务目录。
> 更多信息：<https://manned.org/runsvdir.8>。

- 以当前用户身份启动和管理目录中的所有服务：

`runsvdir {{path/to/services}}`

- 以 root 用户身份启动和管理目录中的所有服务：

`sudo runsvdir {{path/to/services}}`

- 在不同会话中启动服务：

`runsvdir -P {{path/to/services}}`