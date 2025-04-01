# lvextend

> 增加逻辑卷的大小。
> 参见：`lvm`。
> 更多信息：<https://manned.org/lvextend.8>。

- 将卷的大小增加到 120 GB：

`lvextend --size {{120G}} {{逻辑卷}}`

- 将卷的大小增加 40 GB，并同时扩展底层文件系统：

`lvextend --size +{{40G}} -r {{逻辑卷}}`

- 将卷的大小增加到可用物理卷空间的 100%：

`lvextend --size +{{100}}%FREE {{逻辑卷}}`
