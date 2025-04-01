# az bicep

> Bicep CLI 命令组。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/bicep>.

- 安装 Bicep CLI:

`az bicep install`

- 构建 Bicep 文件:

`az bicep build --file {{path/to/file.bicep}}`

- 尝试将 ARM 模板文件反编译为 Bicep 文件:

`az bicep decompile --file {{path/to/template_file.json}}`

- 升级 Bicep CLI 到最新版本:

`az bicep upgrade`

- 显示已安装的 Bicep CLI 版本:

`az bicep version`

- 列出所有可用的 Bicep CLI 版本:

`az bicep list-versions`

- 卸载 Bicep CLI:

`az bicep uninstall`
