# sshfs

> 基于 SSH 的文件系统客户端。
> 更多信息：<https://github.com/libfuse/sshfs>.

- 挂载远程目录:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`

- 卸载远程目录:

`umount {{mountpoint}}`

- 从指定端口的服务器挂载远程目录:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -p {{2222}}`

- 使用压缩:

`sshfs {{username}}@{{remote_host}}:{{remote_directory}} -C`

- 跟随符号链接:

`sshfs -o follow_symlinks {{username}}@{{remote_host}}:{{remote_directory}} {{mountpoint}}`
