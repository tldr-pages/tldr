# volta

> 一个JavaScript工具管理器，用于安装Node.js运行时、npm和Yarn包管理器，或来自npm的任何二进制文件。
> 更多信息：<https://volta.sh>。

- 列出所有已安装的工具：

`volta list`

- 安装工具的最新版本：

`volta install {{node|npm|yarn|package_name}}`

- 安装工具的特定版本：

`volta install {{node|npm|yarn}}@version`

- 为项目选择一个工具版本（将其存储在`package.json`中）：

`volta pin {{node|npm|yarn}}@version`

- 显示帮助信息：

`volta help`

- 显示子命令的帮助信息：

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`