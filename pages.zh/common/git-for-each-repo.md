# git for-each-repo

> 在一组仓库中运行 Git 命令。
> 注意：此命令是实验性的，可能会发生变化。
> 更多信息：<https://git-scm.com/docs/git-for-each-repo>.

- 对 `maintenance.repo` 用户配置变量中列出的每个仓库运行维护命令:

`git for-each-repo --config={{maintenance.repo}} {{maintenance run}}`

- 对全局配置变量中列出的每个仓库运行 `git pull`:

`git for-each-repo --config={{global_configuration_variable}} {{pull}}`