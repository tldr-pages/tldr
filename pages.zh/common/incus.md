# incus

> 现代、安全且强大的系统容器和虚拟机管理器。
> 更多信息：<https://linuxcontainers.org/incus/docs/main>。

- 列出所有容器和虚拟机（包括正在运行和已停止的）：

`incus list`

- 从镜像创建一个容器，并指定自定义名称：

`incus create {{image}} {{container_name}}`

- 启动或停止一个现有容器：

`incus {{start|stop}} {{container_name}}`

- 在已经运行的容器内打开一个 shell：

`incus shell {{container_name}}`

- 删除一个已停止的容器：

`incus delete {{container_name}}`

- 从镜像仓库（远程）拉取一个镜像到本地：

`incus copy {{remote}}:{{image}} local:{{custom_image_name}}`

- 列出官方 `images:` 远程中所有可用的镜像：

`incus image list images:`

- 列出所有已经下载到 `local:` 远程的镜像：

`incus image list local:`