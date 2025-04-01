# dotnet restore

> 恢复 .NET 项目的依赖项和工具。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- 恢复当前目录中的 .NET 项目或解决方案的依赖项：

`dotnet restore`

- 恢复指定位置中的 .NET 项目或解决方案的依赖项：

`dotnet restore {{path/to/project_or_solution}}`

- 恢复依赖项时不缓存 HTTP 请求：

`dotnet restore --no-cache`

- 即使上次恢复成功，也强制解析所有依赖项：

`dotnet restore --force`

- 使用包源失败作为警告来恢复依赖项：

`dotnet restore --ignore-failed-sources`

- 使用特定的详细级别恢复依赖项：

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`