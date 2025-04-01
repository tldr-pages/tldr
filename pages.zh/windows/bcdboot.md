# bcdboot

> 配置或修复启动文件。
> 更多信息：<https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>。

- 使用源 Windows 文件夹中的 BCD 文件初始化系统分区：

`bcdboot {{C:\Windows}}`

- 启用 [v]详细模式：

`bcdboot {{C:\Windows}} /v`

- 指定系统分区的卷字母：

`bcdboot {{C:\Windows}} /s {{S:}}`

- 指定 [l]语言环境：

`bcdboot {{C:\Windows}} /l {{en-us}}`

- 在复制启动文件到指定卷时指定 [f]固件类型：

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`