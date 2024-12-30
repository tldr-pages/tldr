# sfc

> 检查 Windows 系统文件的完整性。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>。

- 显示有关命令用法的信息：

`sfc`

- 扫描所有系统文件，并在可能的情况下修复任何问题：

`sfc /scannow`

- 扫描所有系统文件，但不尝试修复任何问题：

`sfc /verifyonly`

- 扫描特定文件，并在可能的情况下修复任何问题：

`sfc /scanfile={{path\to\file}}`

- 扫描特定文件，但不尝试修复它：

`sfc /verifyfile={{path\to\file}}`

- 在离线修复时，指定启动目录：

`sfc /offbootdir={{path\to\directory}}`

- 在离线修复时，指定 Windows 目录：

`sfc /offwindir={{path\to\directory}}`