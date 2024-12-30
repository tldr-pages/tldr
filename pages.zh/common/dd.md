# dd

> 转换并复制文件。
> 更多信息：<https://manned.org/dd.1p>。

- 从一个 isohybrid 文件（如 `archlinux-xxx.iso`）创建一个可启动的 USB 驱动器并显示进度：

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- 将一个驱动器克隆到另一个驱动器，使用 4 MiB 的块大小，并在命令终止之前刷新写入：

`dd bs=4194304 conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- 通过使用内核随机驱动程序生成一个特定数量的随机字节文件：

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- 基准测试磁盘的顺序写入性能：

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{path/to/file_1GB}}`

- 创建系统备份，将其保存到 IMG 文件中（可以通过交换 `if` 和 `of` 来恢复），并显示进度：

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`