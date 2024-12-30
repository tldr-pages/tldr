# gocryptfs

> 用Go编写的加密覆盖文件系统。
> 更多信息：<https://github.com/rfjakob/gocryptfs>。

- 初始化加密文件系统：

`gocryptfs -init {{path/to/cipher_dir}}`

- 挂载加密文件系统：

`gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 使用显式主密钥而不是密码挂载：

`gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 更改密码：

`gocryptfs --passwd {{path/to/cipher_dir}}`

- 对一个普通目录创建加密快照：

`gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`