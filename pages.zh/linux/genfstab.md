# genfstab

> Arch Linux 安装脚本，用于生成适合添加到 fstab 文件的输出。
> 更多信息：<https://manned.org/genfstab.8>。

- 基于卷标签显示兼容 fstab 的输出：

`genfstab -L {{path/to/mount_point}}`

- 基于卷 UUID 显示兼容 fstab 的输出：

`genfstab -U {{path/to/mount_point}}`

- 生成 fstab 文件的常用方法，需要 root 权限：

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- 将一个卷追加到 fstab 文件中以便自动挂载：

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`