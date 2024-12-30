# blkdiscard

> 在存储设备上丢弃设备扇区。对SSD非常有用。
> 更多信息：<https://manned.org/blkdiscard>。

- 丢弃设备上的所有扇区，移除所有数据：

`blkdiscard {{/dev/device}}`

- 安全地丢弃设备上的所有块，移除所有数据：

`blkdiscard --secure {{/dev/device}}`

- 丢弃设备的前100MB：

`blkdiscard --length {{100MB}} {{/dev/device}}`