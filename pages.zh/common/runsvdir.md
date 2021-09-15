# runsvdir

> 运行整个目录下的服务。
> 更多信息：<https://manpages.ubuntu.com/manpages/latest/man8/runsvdir.8.html>.

- 以当前用户身份启动和管理目录中的所有服务：

`runsvdir {{目录 / 服务文件}}`

- 以 root 用户身份启动和管理目录中的所有服务：

`sudo runsvdir {{目录 / 服务文件}}`

- 在单独会话中启动服务：

`runsvdir -P {{目录 / 服务文件}}`
