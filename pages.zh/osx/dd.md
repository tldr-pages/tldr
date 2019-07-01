# dd

> 转换并复制文件.

- 从 isohybrid 文件（如archlinux-xxx.iso）制作可用于引导系统启动的USB驱动器.

`dd if={{文件.iso}} of=/dev/{{usb设备}}`

- 将驱动器克隆到具有 4MB 块的另一个驱动器并忽略错误:

`dd if=/dev/{{源设备}} of=/dev/{{目标设备}} bs=4m conv=noerror`

- 使用内核随机驱动程序生成100个随机字节的文件:

`dd if=/dev/urandom of={{目标驱动器,接收随机数据文件名}} bs=100 count=1`

- 对磁盘的写入性能进行基准测试:

`dd if=/dev/zero of={{1GB的文件名}} bs=1024 count=1000000`
