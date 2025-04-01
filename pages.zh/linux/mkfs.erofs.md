# mkfs.erofs

> 在图像中创建 EROFS 文件系统。
> 更多信息：<https://erofs.docs.kernel.org/en/latest/>.

- 基于根目录创建 EROFS 文件系统：

`mkfs.erofs image.erofs root/`

- 创建具有特定 UUID 的 EROFS 图像：

`mkfs.erofs -U {{UUID}} image.erofs root/`

- 创建压缩的 EROFS 图像：

`mkfs.erofs -zlz4hc image.erofs root/`

- 创建所有文件都归根用户所有的 EROFS 图像：

`mkfs.erofs --all-root image.erofs root/`