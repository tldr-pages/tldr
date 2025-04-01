# PSVersionTable

> 一个只读变量（如 `$PSVersionTable`），用于获取当前的 PowerShell 版本。
> 此命令只能在 PowerShell 下运行。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>。

- 打印当前安装的 PowerShell 版本和版本信息的摘要：

`$PSVersionTable`

- 获取 PowerShell 的详细版本号（主版本、次版本、构建号和修订号）：

`$PSVersionTable.PSVersion`

- 列出此 PowerShell 版本支持的所有 PowerShell 脚本版本：

`$PSVersionTable.PSCompatibleVersions`

- 获取当前安装的 PowerShell 版本基于的最新 Git 提交 ID（适用于 PowerShell 6.0 及以上版本）：

`$PSVersionTable.GitCommitId`

- 检查用户运行的是 PowerShell Core（6.0 或以上版本）还是原始的“Windows PowerShell”（5.1 或以下版本）：

`$PSVersionTable.PSEdition`