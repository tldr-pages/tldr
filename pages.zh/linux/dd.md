# dd

> 转换和复制文件。
> 另请参阅：caligula。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- 从 isohybrid 文件（如 `archlinux-xxx.iso`）创建可启动 USB 驱动器并显示进度：

`sudo dd if={{路径/到/文件.iso}} of={{/dev/usb_drive}} status=progress`

- 使用 4 MiB 块大小将驱动器克隆到另一个驱动器，并在命令终止前刷新写入：

`sudo dd bs=4m conv=noerror if={{/dev/source_drive}} of={{/dev/dest_drive}} status=progress`

- 使用内核随机驱动程序生成具有特定数量随机字节的文件：

`sudo dd bs={{100}} count={{1}} if=/dev/urandom of={{路径/到/random_file}}`

- 测试磁盘的写入性能：

`sudo dd bs={{1024}} count={{1000000}} if=/dev/zero of={{路径/到/file_1GB}}`

- 创建系统备份，将其保存为 IMG 文件（以后可以通过交换 `if` 和 `of` 来恢复），并显示进度：

`sudo dd if={{/dev/drive_device}} of={{路径/到/file.img}} status=progress`

- 检查正在进行的 `dd` 操作的进度（从另一个 shell 运行此命令）：

`sudo kill -USR1 $(pgrep ^dd)`
