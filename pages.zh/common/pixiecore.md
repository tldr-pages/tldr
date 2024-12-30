# pixiecore

> 管理机器的网络启动。
> 更多信息：<https://github.com/danderson/netboot/tree/master/pixiecore>。

- 启动一个提供 `netboot.xyz` 启动镜像的 PXE 启动服务器：

`pixiecore {{quick}} xyz --dhcp-no-bind`

- 启动一个提供 Ubuntu 启动镜像的新 PXE 启动服务器：

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- 列出快速模式下所有可用的启动镜像：

`pixiecore quick --help`