# dotnet build

> 构建一个 .NET 应用程序及其依赖项。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-build>。

- 在当前目录中编译项目或解决方案：

`dotnet build`

- 在调试模式下编译 .NET 项目或解决方案：

`dotnet build {{path/to/project_or_solution}}`

- 在发布模式下编译：

`dotnet build --configuration {{Release}}`

- 在不恢复依赖项的情况下编译：

`dotnet build --no-restore`

- 使用特定的详细级别编译：

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- 为特定运行时编译：

`dotnet build --runtime {{runtime_identifier}}`

- 指定输出目录：

`dotnet build --output {{path/to/directory}}`