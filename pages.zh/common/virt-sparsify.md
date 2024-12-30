# virt-sparsify

> 使虚拟机驱动映像变为薄配置。
> 注意：仅对离线机器使用，以避免数据损坏。
> 更多信息：<https://libguestfs.org>。

- 从一个未稀疏的映像创建一个没有快照的稀疏压缩映像：

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}`

- 原地稀疏化映像：

`virt-sparsify --in-place {{path/to/image.img}}`