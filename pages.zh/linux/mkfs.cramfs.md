# mkfs.cramfs

> 创建一个ROM文件系统，放置在分区内。
> 更多信息： <https://manned.org/mkfs.cramfs>.

- 在设备b的分区1内创建一个ROM文件系统 (`sdb1`):

`mkfs.cramfs {{/dev/sdb1}}`

- 创建一个带有卷名的ROM文件系统:

`mkfs.cramfs -n {{volume_name}} {{/dev/sdb1}}`
