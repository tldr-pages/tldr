# dotnet 恢复

> 恢复 .NET 项目的依赖项和工具。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>。

- 在当前目录中恢复 .NET 项目或解决方案的依赖项：

`dotnet 恢复`

- 在特定位置恢复 .NET 项目或解决方案的依赖项：

`dotnet 恢复 {{path/to/project_or_solution}}`

- 恢复依赖项时不缓存 HTTP 请求：

`dotnet 恢复 --no-cache`

- 强制解析所有依赖项，即使上次恢复成功：

`dotnet 恢复 --force`

- 将包源失败作为警告恢复依赖项：

`dotnet 恢复 --ignore-failed-sources`

- 以特定的详细级别恢复依赖项：

`dotnet 恢复 --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`