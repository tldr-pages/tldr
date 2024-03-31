# mkfs.ext4

> 在分区内创建一个ext4文件系统。
> 更多信息： <https://manned.org/mkfs.ext4>.

- 在设备b的分区1内创建一个ext4文件系统 (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- 创建一个带有卷标签的ext4文件系统:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdb1}}`
