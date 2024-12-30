# 安装模块

> 从 PowerShell Gallery、NuGet 和其他存储库安装 PowerShell 模块。
> 更多信息请访问：<https://learn.microsoft.com/powershell/module/powershellget/install-module>。

- 安装模块或将其更新到最新可用版本：

`Install-Module {{module}}`

- 安装特定版本的模块：

`Install-Module {{module}} -RequiredVersion {{version}}`

- 安装不早于特定版本的模块：

`Install-Module {{module}} -MinimumVersion {{version}}`

- 指定所需模块的支持版本范围（包含）：

`Install-Module {{module}} -MinimumVersion {{minimum_version}} -MaximumVersion {{maximum_version}}`

- 从特定存储库安装模块：

`Install-Module {{module}} -Repository {{repository}}`

- 从特定存储库安装模块：

`Install-Module {{module}} -Repository {{repository1 , repository2 , ...}}`

- 为所有用户/当前用户安装模块：

`Install-Module {{module}} -Scope {{AllUsers|CurrentUser}}`

- 执行干运行以确定通过 `Install-Module` 将安装、升级或移除哪些模块：

`Install-Module {{module}} -WhatIf`