# dotnet 工具

> 管理 .NET 工具并搜索在 NuGet 上发布的工具。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/global-tools>。

- 安装一个全球工具（对于本地工具不要使用 `--global`）：

`dotnet tool install --global {{dotnetsay}}`

- 安装在本地工具清单中定义的工具：

`dotnet tool restore`

- 更新特定的全球工具（对于本地工具不要使用 `--global`）：

`dotnet tool update --global {{tool_name}}`

- 卸载一个全球工具（对于本地工具不要使用 `--global`）：

`dotnet tool uninstall --global {{tool_name}}`

- 列出已安装的全球工具（对于本地工具不要使用 `--global`）：

`dotnet tool list --global`

- 在 NuGet 中搜索工具：

`dotnet tool search {{search_term}}`

- 显示帮助：

`dotnet tool --help`