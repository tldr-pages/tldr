# nvm

> 安装、卸载或切换 Node.js 版本。
> 支持像 "12.8" 或 "v16.13.1" 这样的版本号，以及 "stable"、"system" 等标签。
> 参见：`asdf`。
> 更多信息：<https://github.com/creationix/nvm>。

- 安装特定版本的 Node.js：

`nvm install {{node_version}}`

- 在当前 shell 中使用特定版本的 Node.js：

`nvm use {{node_version}}`

- 设置默认的 Node.js 版本：

`nvm alias default {{node_version}}`

- 列出所有可用的 Node.js 版本，并高亮显示默认版本：

`nvm list`

- 卸载指定的 Node.js 版本：

`nvm uninstall {{node_version}}`

- 启动特定版本的 Node.js 的 REPL：

`nvm run {{node_version}} --version`

- 在特定版本的 Node.js 中执行脚本：

`nvm exec {{node_version}} node {{app.js}}`
