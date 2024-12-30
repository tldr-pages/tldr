# 获取节点版本

> 列出已安装和可用的 Node.js 版本以供 `ps-nvm` 使用。
> 这是 `ps-nvm` 的一部分，仅可在 PowerShell 下运行。
> 更多信息：<https://github.com/aaronpowell/ps-nvm>。

- 列出所有已安装的 Node.js 版本：

`Get-NodeVersions`

- 列出所有可用的 Node.js 版本：

`Get-NodeVersions -Remote`

- 列出所有可用的 Node.js 20.x 版本：

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`