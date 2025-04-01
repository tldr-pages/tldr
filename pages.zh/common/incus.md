# incus

> 现代、安全且强大的系统容器和虚拟机管理器。
> 更多信息：<https://linuxcontainers.org/incus/docs/main>.

- 列出所有容器和虚拟机（包括正在运行和已停止的）：

`incus list`

- 从镜像创建一个带有自定义名称的容器：

`incus create {{image}} {{container_name}}`

- 启动或停止现有容器：

`incus {{start|stop}} {{container_name}}`

- 在已运行的容器内打开一个 Shell：

`incus shell {{container_name}}`

- 删除已停止的容器：

`incus delete {{container_name}}`

- 从镜像仓库（远程）拉取镜像到本地：

`incus copy {{remote}}:{{image}} local:{{custom_image_name}}`

- 列出官方 `images:` 远程中的所有可用镜像：

`incus image list images:`

- 列出已下载到 `local:` 远程的所有镜像：

`incus image list local:`