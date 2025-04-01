# cryfs

> 用于云的加密文件系统。
> 更多信息：<https://www.cryfs.org/>.

- 挂载加密文件系统。首次执行时将启动初始化向导：

`cryfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 卸载加密文件系统：

`cryfs-unmount {{path/to/mount_point}}`

- 在闲置10分钟后自动卸载：

`cryfs --unmount-idle {{10}} {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 列出支持的加密算法：

`cryfs --show-ciphers`
