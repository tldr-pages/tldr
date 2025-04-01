# Remove-NodeVersion

> 为 `ps-nvm` 卸载 Node.js 运行时版本。
> 该命令属于 `ps-nvm`，只能在 PowerShell 下运行。
> 更多信息：<https://github.com/aaronpowell/ps-nvm>。

- 卸载指定的 Node.js 版本：

`Remove-NodeVersion {{node_version}}`

- 卸载多个 Node.js 版本：

`Remove-NodeVersion {{node_version1 , node_version2 , ...}}`

- 卸载所有当前已安装的 Node.js 20.x 版本：

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- 卸载所有当前已安装的 Node.js 版本：

`Get-NodeVersions | Remove-NodeVersion`