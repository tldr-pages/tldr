# nvm

> 安装、卸载或切换 Node.js 版本。
> 支持如 "12.8" 或 "v16.13.1" 等版本号，以及 "node"、"system" 等标签。
> 另请参阅：`asdf`。
> 更多信息：<https://github.com/nvm-sh/nvm#usage>。

- 安装/卸载指定版本的 Node.js：

`nvm {{install|uninstall}} {{node_版本}}`

- 在当前 shell 中使用指定版本的 Node.js：

`nvm use {{node_版本}}`

- 设置默认的 Node.js 版本：

`nvm alias default {{node_版本}}`

- 列出可安装的远程版本，仅显示 LTS（长期支持）版本：

`nvm ls-remote --lts`

- 列出已安装的版本：

`nvm {{[ls|list]}}`

- 启动指定版本 Node.js 的交互式命令行：

`nvm run {{node_版本}}`

- 使用指定版本的 Node.js 执行脚本：

`nvm exec {{node_版本}} node {{路径/到/脚本.js}}`

- 在当前 Node.js 版本上升级到最新的可用 npm 版本：

`nvm install-latest-npm`
