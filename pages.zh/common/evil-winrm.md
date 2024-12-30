# evil-winrm

> Windows 远程管理 (WinRM) Shell 用于渗透测试。
> 一旦连接，我们将在目标主机上获得 PowerShell 提示符。
> 更多信息：<https://github.com/Hackplayers/evil-winrm>。

- 连接到主机：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}}`

- 连接到主机，传递密码哈希：

`evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}`

- 连接到主机，指定脚本和可执行文件的目录：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}`

- 连接到主机，使用 SSL：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}`

- 将文件上传到主机：

`PS > upload {{path/to/local/file}} {{path/to/remote/file}}`

- 列出所有加载的 PowerShell 函数：

`PS > menu`

- 从 `--scripts` 目录加载一个 PowerShell 脚本：

`PS > {{script.ps1}}`

- 从 `--executables` 目录在主机上调用一个二进制文件：

`PS > Invoke-Binary {{binary.exe}}`