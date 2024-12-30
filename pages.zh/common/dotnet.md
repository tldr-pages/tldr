# dotnet

> 跨平台的 .NET 命令行工具，用于 .NET Core。
> 一些子命令如 `build` 有自己的使用文档。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools>。

- 初始化一个新的 .NET 项目：

`dotnet new {{template_short_name}}`

- 还原 NuGet 包：

`dotnet restore`

- 在当前目录中构建并执行 .NET 项目：

`dotnet run`

- 运行一个打包的 dotnet 应用程序（只需要运行时，其余命令需要安装 .NET Core SDK）：

`dotnet {{path/to/application.dll}}`