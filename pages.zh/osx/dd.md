# dd

> 转换并复制文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/dd.1.html>.

- 从 isohybrid 文件（如 archlinux-xxx.iso）制作可用于引导系统启动的 USB 驱动器：

`dd if={{文件.iso}} of={{/dev/usb 设备}}`

- 将驱动器克隆到具有 4MB 块的另一个驱动器并忽略错误：

`dd bs=4m conv=noerror if={{/dev/源设备}} of={{/dev/目标设备}}`

- 使用内核随机驱动程序生成 100 个随机字节的文件：

`dd bs=100 count={{1}} if=/dev/urandom of={{目标驱动器，接收随机数据文件名}}`

- 对磁盘的写入性能进行基准测试：

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{1GB 的文件名}}`
