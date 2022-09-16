# git

> 分布式版本控制系统。
> 类似如 commit、add、branch、checkout、push 等子命令都有自己的使用文档，可以通过 tldr git subcommand（子命令）的形式查阅。
> 更多信息：<https://git-scm.com/>.

- 检查 git 的版本号：
 
`git --version`

- 显示帮助文档：

`git --help`

- 显示 git subcommand（子命令）的详细帮助文档（如 clone, add, push, log 等子命令）：
    
`git help subcommand`

- 执行 git 的 subcommand（子命令）:

`git subcommand`

- 在自定义的 git 仓库根路径下执行 subcommand（子命令）：

`git -C path/to/repo subcommand`

- 在给定参数条件下，执行 git 的 subcommand（子命令）：

`git -c 'config.key=value' subcommand`