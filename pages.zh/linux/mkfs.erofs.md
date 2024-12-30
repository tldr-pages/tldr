# mkfs.erofs

> 在镜像中创建 EROFS 文件系统。
> 更多信息：<https://erofs.docs.kernel.org/en/latest/>。

- 基于根目录创建 EROFS 文件系统：

`mkfs.erofs image.erofs root/`

- 使用特定 UUID 创建 EROFS 镜像：

`mkfs.erofs -U {{UUID}} image.erofs root/`

- 创建一个压缩的 EROFS 镜像：

`mkfs.erofs -zlz4hc image.erofs root/`

- 创建一个所有文件均由 root 拥有的 EROFS 镜像：

`mkfs.erofs --all-root image.erofs root/`