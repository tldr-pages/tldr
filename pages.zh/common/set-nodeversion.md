# Set-NodeVersion

> 设置 `ps-nvm` 的默认 Node.js 版本。
> 作为 `ps-nvm` 的一部分，只能在 PowerShell 下运行。
> 更多信息：<https://github.com/aaronpowell/ps-nvm>。

- 在当前 PowerShell 会话中使用指定版本的 Node.js：

`Set-NodeVersion {{node_version}}`

- 使用已安装的最新 Node.js 20.x 版本：

`Set-NodeVersion ^20`

- 为当前用户设置默认的 Node.js 版本（仅适用于未来的 PowerShell 会话）：

`Set-NodeVersion {{node_version}} -Persist User`

- 为所有用户设置默认的 Node.js 版本（必须以管理员/根用户身份运行，仅适用于未来的 PowerShell 会话）：

`Set-NodeVersion {{node_version}} -Persist Machine`
