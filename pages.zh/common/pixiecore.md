# pixiecore

> 管理机器的网络启动。
> 更多信息：<https://github.com/danderson/netboot/tree/master/pixiecore>。

- 启动一个 PXE 引导服务器，提供 `netboot.xyz` 引导镜像：

`pixiecore {{quick}} xyz --dhcp-no-bind`

- 启动一个新的 PXE 引导服务器，提供 Ubuntu 引导镜像：

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- 列出快速模式下所有可用的引导镜像：

`pixiecore quick --help`