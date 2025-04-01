# Remove-AppxPackage

> 一个 PowerShell 工具，用于从用户账户中删除应用程序包。
> 更多信息：<https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- 删除应用程序包：

`Remove-AppxPackage {{package}}`

- 为特定用户删除应用程序包：

`Remove-AppxPackage {{package}} -User {{username}}`

- 为所有用户删除应用程序包：

`Remove-AppxPackage {{package}} -AllUsers`

- 删除应用程序包但保留应用数据：

`Remove-AppxPackage {{package}} -PreserveApplicationData`