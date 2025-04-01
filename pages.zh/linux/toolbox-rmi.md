# toolbox rmi

> 移除 `toolbox` 镜像。
> 参见：`toolbox rm`。
> 更多信息：<https://manned.org/toolbox-rmi.1>。

- 移除一个或多个 `toolbox` 镜像：

`toolbox rmi {{image_name1 image_name2 ...}}`

- 移除所有 `toolbox` 镜像：

`toolbox rmi --all`

- 强制移除正在被容器使用的 `toolbox` 镜像（该容器也将被移除）：

`toolbox rmi --force {{image_name}}`