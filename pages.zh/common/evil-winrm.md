# evil-winrm

> 用于渗透测试的 Windows 远程管理 (WinRM) shell。
> 连接后，我们会在目标主机上获得 PowerShell 提示符。
> 更多信息：<https://github.com/Hackplayers/evil-winrm>。

- 连接到主机：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}}`

- 使用密码哈希连接到主机：

`evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}`

- 连接到主机，指定脚本和可执行文件的目录：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}`

- 使用 SSL 连接到主机：

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}`

- 将文件上传到主机：

`PS > upload {{path/to/local/file}} {{path/to/remote/file}}`

- 列出所有已加载的 PowerShell 函数：

`PS > menu`

- 从 `--scripts` 目录加载 PowerShell 脚本：

`PS > {{script.ps1}}`

- 从 `--executables` 目录调用主机上的二进制文件：

`PS > Invoke-Binary {{binary.exe}}`