# virt-sparsify

> 使虚拟机磁盘映像精简置备。
> 注意：仅用于离线机器，以避免数据损坏。
> 更多信息：<https://libguestfs.org>.

- 从一个未精简化的映像创建一个未包含快照的精简压缩映像：

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}`

- 在原位置精简化一个映像：

`virt-sparsify --in-place {{path/to/image.img}}`