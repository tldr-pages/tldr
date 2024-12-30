# lsblk

> 列出设备信息。
> 更多信息：<https://manned.org/lsblk>。

- 以树状格式列出所有存储设备：

`lsblk`

- 也列出空设备：

`lsblk -a`

- 以字节为单位打印 SIZE 列，而不是以人类可读的格式：

`lsblk -b`

- 输出文件系统信息：

`lsblk -f`

- 使用 ASCII 字符进行树形格式化：

`lsblk -i`

- 输出块设备拓扑的信息：

`lsblk -t`

- 排除由逗号分隔的主要设备编号列表指定的设备：

`lsblk -e {{1,7,...}}`

- 使用逗号分隔的列列表显示自定义摘要：

`lsblk --output {{NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...}}`