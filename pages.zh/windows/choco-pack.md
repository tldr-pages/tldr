# choco pack

> 将 NuGet 规范打包为 `nupkg` 文件。
> 更多信息：<https://chocolatey.org/docs/commands-pack>。

- 将 NuGet 规范打包为 `nupkg` 文件：

`choco pack {{path\to\specification_file}}`

- 打包 NuGet 规范并指定生成文件的版本：

`choco pack {{path\to\specification_file}} --version {{version}}`

- 将 NuGet 规范打包到特定目录：

`choco pack {{path\to\specification_file}} --output-directory {{path\to\output_directory}}`