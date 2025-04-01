# rclone

> 将文件或目录复制、同步或移动到多个云服务或从云服务移动。
> 更多信息：<https://rclone.org>.

- 启动 rclone 的交互式配置菜单：

`rclone config`

- 列出 rclone 远程目录的内容：

`rclone lsf {{remote_name}}:{{path/to/directory}}`

- 将本地机器上的文件或目录复制到远程目的地：

`rclone copy {{path/to/source_file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- 将本地机器上在过去 24 小时内更改的文件复制到远程，每操作一个文件都询问用户：

`rclone copy --interactive --max-age 24h {{remote_name}}:{{path/to/directory}} {{path/to/local_directory}}`

- 镜像特定的文件或目录（注意：与复制不同，同步会从远程位置删除不存在于本地的文件）：

`rclone sync {{path/to/file_or_directory}} {{remote_name}}:{{path/to/directory}}`

- 删除远程文件或目录（注意：`--dry-run` 意味着测试，移除此选项以实际删除）：

`rclone --dry-run delete {{remote_name}}:{{path/to/file_or_directory}}`

- 挂载 rclone 远程位置（实验性）：

`rclone mount {{remote_name}}:{{path/to/directory}} {{path/to/mount_point}}`

- 如果 `<Ctrl c>` 失败，卸载 rclone 远程位置（实验性）：

`fusermount -u {{path/to/mount_point}}`