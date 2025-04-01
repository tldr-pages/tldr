# growpart

> 扩展磁盘或磁盘镜像中的分区以填充可用空间。
> 更多信息：<https://github.com/canonical/cloud-utils>.

- 扩展来自 `sdX` 的分区 `n` 以填充到磁盘末尾或下一个分区开始前的空闲空间：

`growpart {{/dev/sdX}} {{n}}`

- 显示在磁盘镜像中扩展分区 `n` 时将要进行的修改：

`growpart --dry-run {{/path/to/disk.img}} {{n}}`