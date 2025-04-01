# dotnet build

> 构建 .NET 应用程序及其依赖项。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- 编译当前目录中的项目或解决方案：

`dotnet build`

- 以调试模式编译 .NET 项目或解决方案：

`dotnet build {{path/to/project_or_solution}}`

- 以发布模式编译：

`dotnet build --configuration {{Release}}`

- 编译时不恢复依赖项：

`dotnet build --no-restore`

- 使用特定的详细级别编译：

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- 为特定的运行时编译：

`dotnet build --runtime {{runtime_identifier}}`

- 指定输出目录：

`dotnet build --output {{path/to/directory}}`