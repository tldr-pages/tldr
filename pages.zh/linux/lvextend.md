# lvextend

> 增加逻辑卷的大小。
> 另见：`lvm`。
> 更多信息：<https://manned.org/lvextend.8>。

- 将卷的大小增加到 120 GB：

`lvextend --size {{120G}} {{logical_volume}}`

- 将卷的大小增加 40 GB，并且更新底层文件系统：

`lvextend --size +{{40G}} -r {{logical_volume}}`

- 将卷的大小增加到物理卷可用空间的 100%：

`lvextend --size +{{100}}%FREE {{logical_volume}}`