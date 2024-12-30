# crictl

> CRI兼容容器运行时的命令行工具。
> 更多信息：<https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md>。

- 列出所有Kubernetes pod（就绪和未就绪）：

`crictl pods`

- 列出所有容器（运行中和已退出）：

`crictl ps --all`

- 列出所有镜像：

`crictl images`

- 打印特定容器的信息：

`crictl inspect {{container_id1 container_id2 ...}}`

- 在运行的容器中打开特定的shell：

`crictl exec -it {{container_id}} {{sh}}`

- 从注册表中拉取特定镜像：

`crictl pull {{image:tag}}`

- 打印并[f]ollow特定容器的日志：

`crictl logs -f {{container_id}}`

- 删除一个或多个镜像：

`crictl rmi {{image_id1 image_id2 ...}}`