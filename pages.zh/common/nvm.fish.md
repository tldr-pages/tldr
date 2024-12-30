# nvm

> 在 fish shell 中安装、卸载或切换 Node.js 版本。
> 支持版本号如 "12.8" 或 "v16.13.1"，以及标签如 "stable"、"system" 等。
> 更多信息：<https://github.com/jorgebucaran/nvm.fish>。

- 安装特定版本的 Node.js：

`nvm install {{node_version}}`

- 在当前 shell 中使用特定版本的 Node.js：

`nvm use {{node_version}}`

- 设置默认的 Node.js 版本：

`set nvm_default_version {{node_version}}`

- 列出所有可用的 Node.js 版本并突出显示默认版本：

`nvm list`

- 卸载给定的 Node.js 版本：

`nvm uninstall {{node_version}}`