# mkfs.ntfs

> 在分区内创建一个NTFS文件系统。
> 更多信息： <https://manned.org/mkfs.ntfs>.

- 在设备b的分区1内创建一个NTFS文件系统 (`sdb1`):

`mkfs.ntfs {{/dev/sdb1}}`

- 创建一个带有卷标签的文件系统:

`mkfs.ntfs -L {{volume_label}} {{/dev/sdb1}}`

- 创建一个带有特定UUID的文件系统:

`mkfs.ntfs -U {{UUID}} {{/dev/sdb1}}`
