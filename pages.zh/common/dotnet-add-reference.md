# dotnet add reference

> 添加 .NET 项目引用。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

- 向当前目录的项目添加引用：

`dotnet add reference {{path/to/reference.csproj}}`

- 向当前目录的项目添加多个引用：

`dotnet add reference {{path/to/reference1.csproj path/to/reference2.csproj ...}}`

- 向特定项目添加引用：

`dotnet add {{path/to/project.csproj}} reference {{path/to/reference.csproj}}`

- 向特定项目添加多个引用：

`dotnet add {{path/to/project.csproj}} reference {{path/to/reference1.csproj path/to/reference2.csproj ...}}`