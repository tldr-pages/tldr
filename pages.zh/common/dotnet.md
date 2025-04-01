# dotnet

> 用于 .NET Core 的跨平台 .NET 命令行工具。
> 一些子命令（如 `build`）有自己的使用文档。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools>。

- 初始化一个新的 .NET 项目：

`dotnet new {{template_short_name}}`

- 恢复 NuGet 包：

`dotnet restore`

- 构建并运行当前目录中的 .NET 项目：

`dotnet run`

- 运行打包的 dotnet 应用程序（只需要运行时，其他命令需要安装 .NET Core SDK）：

`dotnet {{path/to/application.dll}}`
