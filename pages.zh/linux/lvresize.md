# lvresize

> 更改逻辑卷的大小。
> 参见：`lvm`。
> 更多信息：<https://manned.org/lvresize>.

- 将逻辑卷的大小更改为 120 GB：

`lvresize --size {{120G}} {{volume_group}}/{{logical_volume}}`

- 将逻辑卷及其底层文件系统的大小扩展 120 GB：

`lvresize --size +{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

- 将逻辑卷的大小扩展到物理卷的 100% 空间：

`lvresize --size {{100}}%FREE {{volume_group}}/{{logical_volume}}`

- 将逻辑卷及其底层文件系统的大小减少 120 GB：

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`
