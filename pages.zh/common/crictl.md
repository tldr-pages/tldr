# crictl

> 针对 CRI 兼容容器运行时的命令行工具。
> 更多信息：<https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>.

- 列出所有 Kubernetes 容器组（包括 Ready 和 NotReady 状态）：

`crictl pods`

- 列出所有容器（包括 Running 和 Exited 状态）：

`crictl ps --all`

- 列出所有镜像：

`crictl images`

- 打印特定容器的详细信息：

`crictl inspect {{container_id1 container_id2 ...}}`

- 在运行中的容器中打开特定的 shell：

`crictl exec -it {{container_id}} {{sh}}`

- 从镜像仓库中拉取特定的镜像：

`crictl pull {{image:tag}}`

- 打印并 [f]跟踪特定容器的日志：

`crictl logs -f {{container_id}}`

- 删除一个或多个镜像：

`crictl rmi {{image_id1 image_id2 ...}}`
