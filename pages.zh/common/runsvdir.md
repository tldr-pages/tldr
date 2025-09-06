# runsvdir

> 运行整个目录下的服务。
> 更多信息：<https://manned.org/runsvdir.8>.

- 以当前用户身份启动和管理目录中的所有服务：

`runsvdir {{路径/到/服务目录}}`

- 以 root 用户身份启动和管理目录中的所有服务：

`sudo runsvdir {{路径/到/服务目录}}`

- 在单独会话中启动服务：

`runsvdir -P {{路径/到/服务目录}}`
