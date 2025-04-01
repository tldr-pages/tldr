# portablectl

> 用于在 Linux 系统上管理和部署可移植服务镜像的 systemd 工具。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/portablectl.html>.

- 列出在可移植镜像搜索路径中发现的可用可移植服务镜像：

`portablectl list`

- 将可移植服务镜像附加到主机系统：

`portablectl attach {{path/to/image}}`

- 从主机系统分离可移植服务镜像：

`portablectl detach {{path/to/image|image_name}}`

- 显示指定可移植服务镜像的详细信息和元数据：

`portablectl inspect {{path/to/image}}`

- 检查可移植服务镜像是否已附加到主机系统：

`portablectl is-attached {{path/to/image|image_name}}`
