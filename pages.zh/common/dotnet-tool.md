# dotnet tool

> 管理 .NET 工具并在 NuGet 中搜索已发布的工具。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/global-tools>。

- 安装全局工具（本地工具不要使用 `--global`）：

`dotnet tool install --global {{dotnetsay}}`

- 安装本地工具清单中定义的工具：

`dotnet tool restore`

- 更新特定的全局工具（本地工具不要使用 `--global`）：

`dotnet tool update --global {{tool_name}}`

- 卸载全局工具（本地工具不要使用 `--global`）：

`dotnet tool uninstall --global {{tool_name}}`

- 列出已安装的全局工具（本地工具不要使用 `--global`）：

`dotnet tool list --global`

- 在 NuGet 中搜索工具：

`dotnet tool search {{search_term}}`

- 显示帮助：

`dotnet tool --help`
