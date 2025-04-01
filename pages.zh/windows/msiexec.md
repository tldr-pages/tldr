# msiexec

> 使用 MSI 和 MSP 包文件安装、更新、修复或卸载 Windows 程序。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- 从 MSI 包安装程序：

`msiexec /package {{path\to\file.msi}}`

- 从网站安装 MSI 包：

`msiexec /package {{https://example.com/installer.msi}}`

- 安装 MSP 补丁文件：

`msiexec /update {{path\to\file.msp}}`

- 使用相应的 MSI 或 MSP 文件卸载程序或补丁：

`msiexec /uninstall {{path\to\file}}`