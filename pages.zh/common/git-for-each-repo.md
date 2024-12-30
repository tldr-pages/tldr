# git for-each-repo

> 在一系列存储库上运行 Git 命令。
> 注意：此命令仍在实验阶段，可能会有所更改。
> 更多信息：<https://git-scm.com/docs/git-for-each-repo>。

- 在存储在 `maintenance.repo` 用户配置变量中的每个存储库上运行维护：

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- 在全局配置变量中列出的每个存储库上运行 `git pull`：

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`