# fscrypt

> 用于管理Linux文件系统加密的Go工具。
> 更多信息：<https://github.com/google/fscrypt>。

- 为fscrypt准备根文件系统：

`fscrypt setup`

- 为目录启用文件系统加密：

`fscrypt encrypt {{path/to/directory}}`

- 解锁加密目录：

`fscrypt unlock {{path/to/encrypted_directory}}`

- 锁定加密目录：

`fscrypt lock {{path/to/encrypted_directory}}`