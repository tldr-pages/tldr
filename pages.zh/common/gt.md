# gt

> 为 Git 和 GitHub 创建和管理依赖代码更改（堆栈）的序列。
> 更多信息：<https://graphite.dev/docs/get-started>.

- 为当前目录中的仓库初始化 `gt`：

`gt init`

- 在当前分支之上创建一个新分支并提交已暂存的更改：

`gt create {{branch_name}}`

- 创建一个新的提交并修复堆栈中的分支：

`gt modify -cam {{commit_message}}`

- 强制推送当前堆栈中的所有分支到 GitHub 并创建或更新拉取请求：

`gt stack submit`

- 切换到不同的分支（省略分支名称时提示交互模式）：

`gt co {{branch_name}}`

- 与远程版本同步堆栈（也会删除已合并的分支）：

`gt sync`

- 记录所有跟踪的堆栈：

`gt log short`

- 显示指定子命令的帮助：

`gt {{subcommand}} --help`
