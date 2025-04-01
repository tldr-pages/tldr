# dotnet run

> 无需显式编译或启动命令即可运行 .NET 应用程序。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-run>。

- 运行当前目录中的项目：

`dotnet run`

- 运行特定项目：

`dotnet run --project {{path/to/file.csproj}}`

- 使用特定参数运行项目：

`dotnet run -- {{arg1=foo arg2=bar ...}}`

- 使用目标框架别名运行项目：

`dotnet run --framework {{net7.0}}`

- 指定架构和操作系统（自 .NET 6 起可用，不要与 `--runtime` 选项一起使用）：

`dotnet run --arch {{x86|x64|arm|arm64}} --os {{win|win7|osx|linux|ios|android}}`
