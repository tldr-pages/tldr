# Install-Module

> 从 PowerShell 库、NuGet 和其他仓库安装 PowerShell 模块。
> 更多信息：<https://learn.microsoft.com/powershell/module/powershellget/install-module>.

- 安装模块或将其更新到最新可用版本：

`Install-Module {{module}}`

- 安装具有特定版本的模块：

`Install-Module {{module}} -RequiredVersion {{version}}`

- 安装不早于特定版本的模块：

`Install-Module {{module}} -MinimumVersion {{version}}`

- 指定所需模块的版本范围（包含）：

`Install-Module {{module}} -MinimumVersion {{minimum_version}} -MaximumVersion {{maximum_version}}`

- 从特定仓库安装模块：

`Install-Module {{module}} -Repository {{repository}}`

- 从特定的多个仓库安装模块：

`Install-Module {{module}} -Repository {{repository1 , repository2 , ...}}`

- 为所有用户/当前用户安装模块：

`Install-Module {{module}} -Scope {{AllUsers|CurrentUser}}`

- 执行预演以确定将通过 `Install-Module` 安装、升级或删除哪些模块：

`Install-Module {{module}} -WhatIf`
