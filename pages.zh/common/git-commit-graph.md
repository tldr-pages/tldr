# git commit-graph

> 写入和验证 Git 提交图文件。
> 更多信息：<https://git-scm.com/docs/git-commit-graph>.

- 为仓库本地的 `.git` 目录中的已打包提交写入一个提交图文件：

`git commit-graph write`

- 为所有可及提交写入一个提交图文件：

`git show-ref --hash | git commit-graph write --stdin-commits`

- 为当前提交图文件中的所有提交以及从 `HEAD` 可达的提交写入一个提交图文件：

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
