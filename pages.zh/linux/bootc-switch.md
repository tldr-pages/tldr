# bootc switch

> 指定要启动的新容器镜像引用。
> 更多信息：<https://containers.github.io/bootc/man/bootc-switch.html>。

- 从 registry 更改基础操作系统到新的容器镜像：

`sudo bootc switch {{image}}`

- 从根用户的本地镜像存储更改变基础操作系统到新的容器镜像：

`sudo bootc switch --transport containers-storage {{image}}`

- 从 tarball 中存储的容器镜像更改基础操作系统：

`sudo bootc switch --transport oci-archive {{path/to/image.tar.gz}}`