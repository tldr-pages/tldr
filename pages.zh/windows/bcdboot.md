# bcdboot

> 配置或修复启动文件。
> 更多信息：<https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>。

- 使用源Windows文件夹中的BCD文件初始化系统分区：

`bcdboot {{C:\Windows}}`

- 启用 [v]erbose 模式：

`bcdboot {{C:\Windows}} /v`

- 指定 [s]ystem 分区的卷标：

`bcdboot {{C:\Windows}} /s {{S:}}`

- 指定 [l]ocale：

`bcdboot {{C:\Windows}} /l {{en-us}}`

- 在将启动文件复制到指定卷时指定 [f]irmware 类型：

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`