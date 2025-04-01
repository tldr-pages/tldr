# dockerd

> 用于启动和管理 Docker 容器的持久进程。
> 更多信息：<https://docs.docker.com/reference/cli/dockerd/>.

- 运行 Docker 守护进程：

`dockerd`

- 运行 Docker 守护进程并配置其监听特定的套接字（UNIX 和 TCP）：

`dockerd --host unix://{{path/to/tmp.sock}} --host tcp://{{ip}}`

- 使用特定的守护进程 PID 文件运行：

`dockerd --pidfile {{path/to/pid_file}}`

- 以调试模式运行：

`dockerd --debug`

- 运行并设置特定的日志级别：

`dockerd --log-level {{debug|info|warn|error|fatal}}`
