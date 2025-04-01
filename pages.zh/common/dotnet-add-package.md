# dotnet add package

> 在项目文件中添加或更新 .NET 包引用。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

- 向当前目录的项目添加包：

`dotnet add package {{package}}`

- 向特定项目添加包：

`dotnet add {{path/to/file.csproj}} package {{package}}`

- 向项目添加特定版本的包：

`dotnet add package {{package}} --version {{1.0.0}}`

- 使用特定的 NuGet 源添加包：

`dotnet add package {{package}} --source {{https://api.nuget.org/v3/index.json}}`

- 仅在针对特定框架时添加包：

`dotnet add package {{package}} --framework {{net7.0}}`

- 添加包并指定恢复包的目录（默认为 `~/.nuget/packages`）：

`dotnet add package {{package}} --package-directory {{path/to/directory}}`
