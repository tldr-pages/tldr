# repair-bde

> 尝试修复或解密损坏的 BitLocker 加密卷。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- 尝试修复一个指定的卷：

`repair-bde {{C:}}`

- 尝试修复指定的卷并输出到另一个卷：

`repair-bde {{C:}} {{D:}}`

- 尝试使用提供的恢复密钥文件修复指定的卷：

`repair-bde {{C:}} -RecoveryKey {{bek 文件的路径}}`

- 尝试使用提供的数字恢复密码修复指定的卷：

`repair-bde {{C:}} -RecoveryPassword {{密码}}`

- 尝试使用提供的密码修复指定的卷：

`repair-bde {{C:}} -Password {{密码}}`

- 尝试使用提供的密钥包修复指定的卷：

`repair-bde {{C:}} -KeyPackage {{目录的路径}}`

- 将日志输出到指定的文件：

`repair-bde {{C:}} -LogFile {{文件的路径}}`

- 显示所有可用的选项：

`repair-bde /?`
