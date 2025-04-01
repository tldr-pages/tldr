# Install-NodeVersion

> 为 `ps-nvm` 安装 Node.js 运行时版本。
> 此命令是 `ps-nvm` 的一部分，只能在 PowerShell 下运行。
> 更多信息：<https://github.com/aaronpowell/ps-nvm>.

- 安装特定的 Node.js 版本：

`Install-NodeVersion {{node_version}}`

- 安装多个 Node.js 版本：

`Install-NodeVersion {{node_version1 , node_version2 , ...}}`

- 安装最新可用的 Node.js 20 版本：

`Install-NodeVersion ^20`

- 安装 Node.js 的 x86 (x86 32位) / x64 (x86 64位) / arm64 (ARM 64位) 版本：

`Install-NodeVersion {{node_version}} -Architecture {{x86|x64|arm64}}`

- 使用 HTTP 代理下载 Node.js：

`Install-NodeVersion {{node-version}} -Proxy {{http://example.com}}`
