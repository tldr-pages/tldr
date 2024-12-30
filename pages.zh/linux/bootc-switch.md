# bootc 切换

> 目标是启动一个新的容器镜像引用。
> 更多信息：<https://containers.github.io/bootc/man/bootc-switch.html>。

- 将基础操作系统更改为来自注册表的新容器镜像：

`sudo bootc switch {{image}}`

- 将基础操作系统更改为来自根用户的本地镜像存储的新容器镜像：

`sudo bootc switch --transport containers-storage {{image}}`

- 将基础操作系统更改为存储在 tarball 中的新容器镜像：

`sudo bootc switch --transport oci-archive {{path/to/image.tar.gz}}`