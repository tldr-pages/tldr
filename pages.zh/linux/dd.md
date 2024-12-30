# dd

> 转换并复制文件。
> 更多信息：<https://www.gnu.org/software/coreutils/dd>。

- 从一个 isohybrid 文件（例如 `archlinux-xxx.iso`）创建一个可启动的 USB 驱动器，并显示进度：

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- 将一个驱动器克隆到另一个驱动器，使用 4 MiB 的块大小，并在命令终止前刷新写入：

`dd bs=4M conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- 使用内核随机驱动生成一个具有特定数量随机字节的文件：

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- 基准测试磁盘的写入性能：

`dd bs={{1M}} count={{1024}} if=/dev/zero of={{path/to/file_1GB}}`

- 创建系统备份，将其保存到 IMG 文件（可以通过交换 `if` 和 `of` 后进行恢复），并显示进度：

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- 检查正在进行的 `dd` 操作的进度（从另一个 shell 运行此命令）：

`kill -USR1 $(pgrep -x dd)`