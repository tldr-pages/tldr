# krunvm

> 从 OCI 镜像创建 MicroVM。
> 更多信息：<https://github.com/containers/krunvm>。

- 基于 Fedora 创建 MicroVM：

`krunvm create {{docker.io/fedora}} --cpus {{vcpu数量}} --mem {{内存大小_兆字节}} --name "{{名称}}"`

- 启动特定镜像：

`krunvm start "{{镜像名称}}"`

- 列出镜像：

`krunvm list`

- 修改特定镜像：

`krunvm changevm --cpus {{vcpu数量}} --mem {{内存大小_兆字节}} --name "{{新vm名称}}" "{{当前vm名称}}"`

- 删除特定镜像：

`krunvm delete "{{镜像名称}}"`