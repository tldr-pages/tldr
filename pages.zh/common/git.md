# git

> 分布式版本控制系统。
> 一些子命令如 `commit`、`add`、`branch`、`checkout`、`push` 等有各自的使用文档。
> 更多信息：<https://git-scm.com/>.

- 执行 Git 子命令：

`git {{subcommand}}`

- 在自定义仓库根路径上执行 Git 子命令：

`git -C {{path/to/repo}} {{subcommand}}`

- 使用给定的配置集执行 Git 子命令：

`git -c '{{config.key}}={{value}}' {{subcommand}}`

- 显示帮助：

`git --help`

- 显示特定子命令的帮助（如 `clone`、`add`、`push`、`log` 等）：

`git help {{subcommand}}`

- 显示版本：

`git --version`