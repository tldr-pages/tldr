# corepack

> 零运行时依赖包，充当 Node 项目与其包管理器之间的桥梁。
> 更多信息：<https://github.com/nodejs/corepack>。

- 将 Corepack 适配器添加到 Node.js 安装目录，以便将其作为全局命令使用：

`corepack enable`

- 将 Corepack 适配器添加到特定目录：

`corepack enable --install-directory {{path/to/directory}}`

- 从 Node.js 安装目录中移除 Corepack 适配器：

`corepack disable`

- 准备一个特定的包管理器：

`corepack prepare {{package_manager}}@{{version}} --activate`

- 准备当前路径下为项目配置的包管理器：

`corepack prepare`

- 使用一个包管理器，而不将其安装为全局命令：

`corepack {{npm|pnpm|yarn}} {{package_manager_arguments}}`

- 从指定的归档文件中安装一个包管理器：

`corepack hydrate {{path/to/corepack.tgz}}`

- 显示子命令的帮助信息：

`corepack {{subcommand}} --help`