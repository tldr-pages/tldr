# rclone

> 从许多云服务中复制、同步或移动文件和目录。
> 更多信息：<https://rclone.org>。

- 启动交互式菜单以设置 rclone：

`rclone config`

- 列出 rclone 远程目录的内容：

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- 将文件或目录从本地计算机复制到远程目的地：

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- 从本地计算机将过去 24 小时内更改的文件复制到远程，并要求用户确认每个文件：

`rclone copy --interactive --max-age 24h {{remote_name}}:{{path/to/directory}} {{path/to/local_directory}}`

- 镜像特定文件或目录（注意：与复制不同，sync 会在远程删除本地不存在的文件）：

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- 删除远程文件或目录（注意：`--dry-run` 表示测试，移除该命令以实际删除）：

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}`

- 挂载 rclone 远程（实验性）：

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- 如果 CTRL-C 失败则卸载 rclone 远程（实验性）：

`fusermount -u {{path/to/mount_point}}`