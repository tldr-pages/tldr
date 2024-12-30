# findfs

> 通过标签或UUID查找文件系统。
> 更多信息：<https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>。

- 按文件系统标签搜索块设备：

`findfs LABEL={{label}}`

- 按文件系统UUID搜索：

`findfs UUID={{uuid}}`

- 按分区标签搜索（GPT或MAC分区表）：

`findfs PARTLABEL={{partition_label}}`

- 按分区UUID搜索（仅限GPT分区表）：

`findfs PARTUUID={{partition_uuid}}`