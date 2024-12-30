# toolbox rmi

> 删除 `toolbox` 镜像。
> 另见： `toolbox rm`。
> 更多信息： <https://manned.org/toolbox-rmi.1>。

- 删除一个或多个 `toolbox` 镜像：

`toolbox rmi {{image_name1 image_name2 ...}}`

- 删除所有 `toolbox` 镜像：

`toolbox rmi --all`

- 强制删除当前正在被容器使用的 `toolbox` 镜像（容器也将被删除）：

`toolbox rmi --force {{image_name}}`