# sfc

> 扫描 Windows 系统文件的完整性。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- 显示命令的使用方法：

`sfc`

- 扫描所有的系统文件，如果可能的话，修复所有出现的问题：

`sfc /scannow`

- 扫描系统文件，但不修复出现的问题：

`sfc /verifyonly`

- 扫描指定的文件，如果可能的话，修复所有出现的问题：

`sfc /scanfile={{文件的路径}}`

- 扫描指定的文件，但不修复出现的问题：

`sfc /verifyfile={{文件的路径}}`

- 当离线修复时，指定引导目录：

`sfc /offbootdir={{目录的路径}}`

- 当离线修复时，指定 Windows 目录：

`sfc /offwindir={{文件的路径}}`
