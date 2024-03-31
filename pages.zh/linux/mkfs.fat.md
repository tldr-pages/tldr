# mkfs.fat

> 在分区内创建一个MS-DOS文件系统。
> 更多信息： <https://manned.org/mkfs.fat>.

- 在设备b的分区1内创建一个FAT文件系统 (`sdb1`):

`mkfs.fat {{/dev/sdb1}}`

- 创建一个带有卷名的文件系统:

`mkfs.fat -n {{volume_name}} {{/dev/sdb1}}`

- 创建一个带有卷ID的文件系统:

`mkfs.fat -i {{volume_id}} {{/dev/sdb1}}`

- 使用5个而不是2个文件分配表:

`mkfs.fat -f 5 {{/dev/sdb1}}`
