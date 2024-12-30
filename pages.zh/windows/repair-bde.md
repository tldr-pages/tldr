# repair-bde

> 尝试修复或解密受损的 BitLocker 加密卷。
> 更多信息请访问：<https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>。

- 尝试修复指定的卷：

`repair-bde {{C:}}`

- 尝试修复指定的卷并输出到另一个卷：

`repair-bde {{C:}} {{D:}}`

- 尝试使用提供的恢复密钥文件修复指定的卷：

`repair-bde {{C:}} -RecoveryKey {{path\to\file.bek}}`

- 尝试使用提供的数字恢复密码修复指定的卷：

`repair-bde {{C:}} -RecoveryPassword {{password}}`

- 尝试使用提供的密码修复指定的卷：

`repair-bde {{C:}} -Password {{password}}`

- 尝试使用提供的密钥包修复指定的卷：

`repair-bde {{C:}} -KeyPackage {{path\to\directory}}`

- 将所有输出记录到特定文件：

`repair-bde {{C:}} -LogFile {{path\to\file}}`

- 显示帮助信息：

`repair-bde /?`