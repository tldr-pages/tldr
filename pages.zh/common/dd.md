# dd

> 转换和复制文件。
> 更多信息：<https://manned.org/dd.1p>。

- 从 isohybrid 文件（如 `archlinux-xxx.iso`）制作可启动 USB 驱动器，并显示进度：

`dd if={{路径/到/文件.iso}} of={{/dev/usb_drive}} status=progress`

- 以 4 MiB 块大小克隆驱动器，并在命令终止前刷新写入：

`dd bs=4194304 conv=fsync if={{/dev/源驱动器}} of={{/dev/目标驱动器}}`

- 使用内核随机驱动程序生成包含指定数量随机字节的文件：

`dd bs={{100}} count={{1}} if=/dev/urandom of={{路径/到/随机文件}}`

- 测试磁盘的顺序写入性能：

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{路径/到/文件_1GB}}`

- 创建系统备份并保存为 IMG 文件（之后可通过交换 `if` 和 `of` 恢复），并显示进度：

`dd if={{/dev/驱动器设备}} of={{路径/到/文件.img}} status=progress`
