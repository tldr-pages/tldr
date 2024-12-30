# dd

> 转换并复制文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/dd.1.html>。

- 从一个 isohybrid 文件（例如 `archlinux-xxx.iso`）创建一个可启动的 USB 驱动器，并显示进度：

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- 将一个驱动器克隆到另一个驱动器，使用 4 MB 块，忽略错误并显示进度：

`dd bs=4m conv=noerror if={{/dev/source_drive}} of={{/dev/dest_drive}} status=progress`

- 使用内核随机驱动程序生成一个具有特定字节数的随机文件：

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- 基准测试磁盘的写入性能：

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{path/to/1GB_file}}`

- 创建系统备份，将其保存到 IMG 文件中（可以通过交换 `if` 和 `of` 来恢复），并显示进度：

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- 检查正在进行的 `dd` 操作的进度（从另一个 shell 中运行此命令）：

`kill -USR1 $(pgrep ^dd)`