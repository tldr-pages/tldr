# gt

> 创建和管理依赖代码更改的序列（堆栈）以用于 Git 和 GitHub。
> 更多信息：<https://docs.graphite.dev>。

- 使用 Graphite 的 API 进行 CLI 身份验证：

`gt auth --token {{graphite_cli_auth_token}}`

- 在当前目录中为仓库初始化 `gt`：

`gt repo init`

- 在当前分支之上创建一个新分支并提交暂存的更改：

`gt branch create {{branch_name}}`

- 创建一个新提交并修复上游分支：

`gt commit create -m {{commit_message}}`

- 强制推送当前堆栈中的所有分支到 GitHub 并创建或更新 PR：

`gt stack submit`

- 记录所有跟踪的堆栈：

`gt log short`

- 显示指定子命令的帮助信息：

`gt {{subcommand}} --help`