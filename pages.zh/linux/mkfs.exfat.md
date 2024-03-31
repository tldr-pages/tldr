# mkfs.exfat

> 在分区内创建一个exFAT文件系统。
> 更多信息： <https://manned.org/mkfs.exfat>.

- 在设备b的分区1内创建一个exFAT文件系统 (`sdb1`):

`mkfs.exfat {{/dev/sdb1}}`

- 创建一个带有卷名的文件系统:

`mkfs.exfat -n {{volume_name}} {{/dev/sdb1}}`

- 创建一个带有卷ID的文件系统:

`mkfs.exfat -i {{volume_id}} {{/dev/sdb1}}`
