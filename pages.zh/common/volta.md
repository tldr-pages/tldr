# volta

> 一个 JavaScript 工具管理器，用于安装 Node.js 运行时、npm 和 Yarn 包管理器，或任何来自 npm 的二进制文件。
> 更多信息：<https://volta.sh>.

- 列出所有已安装的工具：

`volta list`

- 安装工具的最新版本：

`volta install {{node|npm|yarn|package_name}}`

- 安装工具的特定版本：

`volta install {{node|npm|yarn}}@version`

- 为项目选择工具的版本（将在 `package.json` 中存储）：

`volta pin {{node|npm|yarn}}@version`

- 显示帮助：

`volta help`

- 显示子命令的帮助：

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`