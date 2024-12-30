# dotnet 添加包

> 在项目文件中添加或更新 .NET 包引用。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>。

- 将包添加到当前目录中的项目：

`dotnet add package {{package}}`

- 将包添加到特定项目：

`dotnet add {{path/to/file.csproj}} package {{package}}`

- 将特定版本的包添加到项目中：

`dotnet add package {{package}} --version {{1.0.0}}`

- 使用特定的 NuGet 源添加包：

`dotnet add package {{package}} --source {{https://api.nuget.org/v3/index.json}}`

- 仅在目标特定框架时添加包：

`dotnet add package {{package}} --framework {{net7.0}}`

- 添加并指定恢复包的目录（默认情况下为 `~/.nuget/packages`）：

`dotnet add package {{package}} --package-directory {{path/to/directory}}`