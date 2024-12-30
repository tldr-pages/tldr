# dotnet 发布

> 将 .NET 应用程序及其依赖项发布到目录中，以便部署到托管系统。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>。

- 以发布模式编译 .NET 项目：

`dotnet publish --configuration Release {{path/to/project_file}}`

- 与您的应用程序一起发布 .NET Core 运行时，以便针对指定的运行时：

`dotnet publish --self-contained true --runtime {{runtime_identifier}} {{path/to/project_file}}`

- 将应用程序打包为特定平台的单文件可执行文件：

`dotnet publish --runtime {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- 剪裁未使用的库以减少应用程序的部署大小：

`dotnet publish --self-contained true --runtime {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- 编译 .NET 项目而不还原依赖项：

`dotnet publish --no-restore {{path/to/project_file}}`

- 指定输出目录：

`dotnet publish --output {{path/to/directory}} {{path/to/project_file}}`