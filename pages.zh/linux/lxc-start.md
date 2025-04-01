# lxc-start

> 启动容器。
> 更多信息：<https://linuxcontainers.org/lxc/getting-started/>.

- 启动 lxc 服务：

`systemctl start lxc-net`

- 启动容器：

`sudo lxc-start {{container_name}}`

- 在前台启动容器：

`sudo lxc-start {{container_name}} {{[-F|--foreground]}}`

- 退出前台容器（在单独的终端中运行此命令）：

`sudo lxc-stop {{container_name}}`

- 显示帮助：

`lxc-start {{[-?|--help]}}`
