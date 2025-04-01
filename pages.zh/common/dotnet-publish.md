# dotnet publish

> 发布 .NET 应用程序及其依赖项到一个目录，以便部署到托管系统。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- 以发布模式编译 .NET 项目：

`dotnet publish --configuration Release {{path/to/project_file}}`

- 为指定的运行时将 .NET Core 运行时与应用程序一起发布：

`dotnet publish --self-contained true --runtime {{runtime_identifier}} {{path/to/project_file}}`

- 将应用程序打包为特定平台的单一文件可执行文件：

`dotnet publish --runtime {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- 剪裁未使用的库以减小应用程序的部署大小：

`dotnet publish --self-contained true --runtime {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- 编译 .NET 项目时不恢复依赖项：

`dotnet publish --no-restore {{path/to/project_file}}`

- 指定输出目录：

`dotnet publish --output {{path/to/directory}} {{path/to/project_file}}`