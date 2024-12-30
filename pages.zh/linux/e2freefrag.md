# e2freefrag

> 打印 ext2/ext3/ext4 文件系统的空闲空间碎片信息。
> 更多信息：<https://manned.org/e2freefrag>。

- 检查存在多少个连续且对齐的空闲块：

`e2freefrag {{/dev/sdXN}}`

- 指定以千字节为单位的块大小，以打印可用的空闲块数量：

`e2freefrag -c {{chunk_size_in_kb}} {{/dev/sdXN}}`