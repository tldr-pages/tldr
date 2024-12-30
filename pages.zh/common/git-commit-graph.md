# git commit-graph

> 编写和验证 Git 提交图文件。
> 更多信息：<https://git-scm.com/docs/git-commit-graph>。

- 为存储库本地 `.git` 目录中的打包提交写入提交图文件：

`git commit-graph write`

- 写入一个包含所有可达提交的提交图文件：

`git show-ref --hash | git commit-graph write --stdin-commits`

- 写入一个包含当前提交图文件中所有提交以及从 `HEAD` 可达的提交的提交图文件：

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`