# systemd-nspawn

> 在轻量级容器中启动命令或操作系统。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- 在容器中运行命令：

`systemd-nspawn --directory {{path/to/container_root}}`

- 在容器中运行完整的基于 Linux 的操作系统：

`systemd-nspawn --boot --directory {{path/to/container_root}}`

- 使用存根初始化进程将指定命令作为 PID 2（而不是 PID 1）在容器中运行：

`systemd-nspawn --directory {{path/to/container_root}} --as-pid2`

- 指定机器名和主机名：

`systemd-nspawn --machine={{container_name}} --hostname={{container_host}} --directory {{path/to/container_root}}`
