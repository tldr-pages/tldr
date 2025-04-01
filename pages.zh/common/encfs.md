# encfs

> 挂载或创建加密的虚拟文件系统。
> 请参见 `fusermount`，它可用于卸载通过此命令挂载的文件系统。
> 更多信息：<https://github.com/vgough/encfs>。

- 初始化或挂载一个加密的文件系统：

`encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- 使用标准设置初始化一个加密的文件系统：

`encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- 在前台运行 encfs 而不是作为守护进程：

`encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- 挂载一个普通目录的加密快照：

`encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
