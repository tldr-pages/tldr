# nvm

> 安装、卸载或切换 Node.js 版本。
> 支持版本号如 "12.8" 或 "v16.13.1"，以及标签如 "stable"、"system" 等。
> 更多信息：<https://github.com/coreybutler/nvm-windows>。

- 安装特定版本的 Node.js：

`nvm install {{node_version}}`

- 设置 Node.js 的默认版本（必须以管理员身份运行）：

`nvm use {{node_version}}`

- 列出所有可用的 Node.js 版本并突出显示默认版本：

`nvm list`

- 列出所有远程 Node.js 版本：

`nvm ls-remote`

- 卸载指定的 Node.js 版本：

`nvm uninstall {{node_version}}`