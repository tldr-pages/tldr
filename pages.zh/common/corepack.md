# corepack

> 无运行时依赖的包，作为 Node 项目和它们的包管理器之间的桥梁。
> 更多信息：<https://github.com/nodejs/corepack>.

- 将 Corepack 的快捷方式添加到 Node.js 安装目录中，以使它们作为全局命令可用：

`corepack enable`

- 将 Corepack 的快捷方式添加到特定目录中：

`corepack enable --install-directory {{path/to/directory}}`

- 从 Node.js 安装目录中删除 Corepack 的快捷方式：

`corepack disable`

- 准备特定的包管理器：

`corepack prepare {{package_manager}}@{{version}} --activate`

- 准备当前路径下项目配置的包管理器：

`corepack prepare`

- 使用包管理器而不将其安装为全局命令：

`corepack {{npm|pnpm|yarn}} {{package_manager_arguments}}`

- 从指定的归档文件安装包管理器：

`corepack hydrate {{path/to/corepack.tgz}}`

- 显示子命令的帮助信息：

`corepack {{subcommand}} --help`