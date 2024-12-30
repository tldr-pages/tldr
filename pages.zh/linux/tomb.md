# 坟墓

> 管理可以安全运输和隐藏在文件系统中的加密存储目录。
> 更多信息：<https://www.dyne.org/software/tomb/>.

- 创建一个初始大小为 100 MB 的新坟墓：

`tomb dig -s {{100}} {{encrypted_directory.tomb}}`

- 创建一个新的密钥文件，可以用于锁定坟墓；用户将被提示输入密钥的密码：

`tomb forge {{encrypted_directory.tomb.key}}`

- 强制创建一个新密钥，即使坟墓不允许密钥生成（由于交换）：

`tomb forge {{encrypted_directory.tomb.key}} -f`

- 使用 `forge` 制作的密钥初始化并锁定一个空的坟墓：

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- 使用其密钥挂载坟墓（默认在 `/media`），使其可用作常规文件系统目录：

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- 关闭坟墓（如果坟墓正被进程使用，则会失败）：

`tomb close {{encrypted_directory.tomb}}`

- 强制关闭所有打开的坟墓，杀死任何使用它们的应用程序：

`tomb slam all`

- 列出所有打开的坟墓：

`tomb list`