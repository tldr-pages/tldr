# nvm

> 在 fish shell 下安装、卸载或切换 Node.js 版本。
> 支持如 "12.8" 或 "v16.13.1" 这样的版本号，以及 "stable"、"system" 等标签。
> 更多信息：<https://github.com/jorgebucaran/nvm.fish>.

- 安装特定版本的 Node.js：

`nvm install {{node_version}}`

- 在当前 shell 中使用特定版本的 Node.js：

`nvm use {{node_version}}`

- 设置默认的 Node.js 版本：

`set nvm_default_version {{node_version}}`

- 列出所有可用的 Node.js 版本，并突出显示默认版本：

`nvm list`

- 卸载指定的 Node.js 版本：

`nvm uninstall {{node_version}}`
