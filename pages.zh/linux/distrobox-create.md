# distrobox-create

> 创建 Distrobox 容器。另见：`tldr distrobox`。
> 创建的容器将与主机紧密集成，允许共享用户的 HOME 目录、外部存储、外部 USB 设备、图形应用（X11/Wayland）和音频。
> 更多信息：<https://distrobox.it/usage/distrobox-create>。

- 使用 Ubuntu 镜像创建 Distrobox 容器：

`distrobox-create {{container_name}} --image {{ubuntu:latest}}`

- 克隆 Distrobox 容器：

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
