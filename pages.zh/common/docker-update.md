# docker update

> 更新 Docker 容器的配置。
> 该命令不支持 Windows 容器。
> 更多信息：<https://docs.docker.com/reference/cli/docker/container/update/>.

- 更新特定容器退出时的应用重启策略：

`docker update --restart={{always|no|on-failure|unless-stopped}} {{container_name}}`

- 更新特定容器退出时的重启策略，非零退出状态时最多重启三次：

`docker update --restart=on-failure:3 {{container_name}}`

- 更新特定容器可用的 CPU 数量：

`docker update --cpus {{count}} {{container_name}}`

- 更新特定容器的内存限制（以 [M] 兆字节为单位）：

`docker update {{[-m|--memory]}} {{limit}}M {{container_name}}`

- 更新特定容器内部允许的最大进程 ID 数量（使用 `-1` 表示无限制）：

`docker update --pids-limit {{count}} {{container_name}}`

- 更新特定容器可以向磁盘交换的内存量（以 [M] 兆字节为单位，使用 `-1` 表示无限制）：

`docker update --memory-swap {{limit}}M {{container_name}}`