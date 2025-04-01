# Add-AppxPackage

> 一个 PowerShell 工具，用于将已签名的应用程序包（`.appx`、`.msix`、`.appxbundle` 和 `.msixbundle`）添加到用户账户中。
> 更多信息：<https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- 添加应用程序包：

`Add-AppxPackage -Path {{path\to\package.msix}}`

- 添加带有依赖项的应用程序包：

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}}`

- 使用应用程序安装文件安装应用程序：

`Add-AppxPackage -AppInstallerFile {{path\to\app.appinstaller}}`

- 添加未签名的包：

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}} -AllowUnsigned`