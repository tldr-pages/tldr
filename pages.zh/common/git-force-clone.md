# git force-clone

> 获取 `git clone` 的基本功能，但如果是目标 Git 仓库已存在，则会将其强制重置以匹配远程仓库。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- 将 Git 仓库克隆到一个新目录中：

`git force-clone {{remote_repository_location}} {{path/to/directory}}`

- 将 Git 仓库克隆到一个新目录中，同时检出指定的分支：

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`

- 将 Git 仓库克隆到一个已存在的 Git 仓库目录中，执行强制重置以匹配远程仓库，并检出指定的分支：

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`
