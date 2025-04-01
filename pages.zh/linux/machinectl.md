# machinectl

> 控制 systemd 机器管理器。
> 对虚拟机、容器和镜像执行操作。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- 使用 `systemd-nspawn` 作为服务启动一台机器：

`sudo machinectl start {{machine_name}}`

- 停止正在运行的机器：

`sudo machinectl stop {{machine_name}}`

- 显示正在运行的机器列表：

`machinectl list`

- 在机器内打开一个交互式 shell：

`sudo machinectl shell {{machine_name}}`
