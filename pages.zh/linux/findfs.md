# findfs

> 通过标签或 UUID 查找文件系统。
> 更多信息：<https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>。

- 通过文件系统标签查找块设备：

`findfs LABEL={{label}}`

- 通过文件系统 UUID 查找：

`findfs UUID={{uuid}}`

- 通过分区标签（GPT 或 MAC 分区表）查找：

`findfs PARTLABEL={{partition_label}}`

- 通过分区 UUID（仅限 GPT 分区表）查找：

`findfs PARTUUID={{partition_uuid}}`