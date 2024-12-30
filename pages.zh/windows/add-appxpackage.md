# 添加-AppxPackage

> 一个 PowerShell 工具，用于将一个签名的应用包（`.appx`、`.msix`、`.appxbundle` 和 `.msixbundle`）添加到用户帐户中。
> 更多信息：<https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>。

- 添加一个应用包：

`Add-AppxPackage -Path {{path\to\package.msix}}`

- 添加一个具有依赖关系的应用包：

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}}`

- 使用应用安装程序文件安装应用：

`Add-AppxPackage -AppInstallerFile {{path\to\app.appinstaller}}`

- 添加一个未签名的包：

`Add-AppxPackage -Path {{path\to\package.msix}} -DependencyPath {{path\to\dependencies.msix}} -AllowUnsigned`