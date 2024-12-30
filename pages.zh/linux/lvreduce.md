# lvreduce

> 减小逻辑卷的大小。
> 另见：`lvm`。
> 更多信息：<https://manned.org/lvreduce>。

- 将卷的大小减少到 120 GB：

`lvreduce --size {{120G}} {{logical_volume}}`

- 将卷的大小减少 40 GB，并同时调整底层文件系统：

`lvreduce --size -{{40G}} -r {{logical_volume}}`