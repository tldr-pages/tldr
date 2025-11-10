# dd

> 转换和复制文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/dd.1.html>.

- 从 isohybrid 文件（如 `archlinux-xxx.iso`）创建可启动 USB 驱动器并显示进度：

`dd if={{路径/到/文件.iso}} of={{/dev/usb_drive}} status=progress`

- 以 4MB 块大小克隆驱动器到另一个驱动器，忽略错误并显示进度：

`dd bs=4m conv=noerror if={{/dev/源驱动器}} of={{/dev/目标驱动器}} status=progress`

- 使用内核随机驱动程序生成具有指定数量随机字节的文件：

`dd bs={{100}} count={{1}} if=/dev/urandom of={{路径/到/随机文件}}`

- 测试磁盘的写入性能：

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{路径/到/1GB文件}}`

- 创建系统备份，保存为 IMG 文件（稍后可通过交换 `if` 和 `of` 参数恢复），并显示进度：

`dd if={{/dev/驱动器设备}} of={{路径/到/文件.img}} status=progress`

- 检查正在进行的 `dd` 操作的进度（在另一个 shell 中运行此命令）：

`kill -USR1 $(pgrep ^dd)`
