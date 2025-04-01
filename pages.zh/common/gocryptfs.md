# gocryptfs

> 使用 Go 语言编写的加密覆盖文件系统。
> 更多信息：<https://github.com/rfjakob/gocryptfs>.

- 初始化一个加密文件系统：

`gocryptfs -init {{path/to/cipher_dir}}`

- 挂载一个加密文件系统：

`gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 使用显式主密钥而不是密码挂载：

`gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}`

- 更改密码：

`gocryptfs --passwd {{path/to/cipher_dir}}`

- 创建一个明文目录的加密快照：

`gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
