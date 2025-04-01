# tomb

> 管理可以在文件系统中安全传输和隐藏的加密存储目录。
> 更多信息：<https://www.dyne.org/software/tomb/>.

- 创建一个新的 100 MB 的墓穴：

`tomb dig -s {{100}} {{encrypted_directory.tomb}}`

- 创建一个新的密钥文件，用于锁定墓穴；用户将被提示输入密钥的密码：

`tomb forge {{encrypted_directory.tomb.key}}`

- 强制创建一个新的密钥文件，即使墓穴不允许创建密钥（由于交换分区的原因）：

`tomb forge {{encrypted_directory.tomb.key}} -f`

- 使用 `forge` 创建的密钥初始化并锁定一个空的墓穴：

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- 使用其密钥挂载墓穴（默认挂载在 `/media`），使其作为常规文件系统目录使用：

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- 关闭墓穴（如果墓穴正在被进程使用，则关闭失败）：

`tomb close {{encrypted_directory.tomb}}`

- 强制关闭所有打开的墓穴，终止使用它们的应用程序：

`tomb slam all`

- 列出所有打开的墓穴：

`tomb list`
