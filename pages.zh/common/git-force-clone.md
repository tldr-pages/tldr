# git 强制克隆

> 获取 `git clone` 的基本功能，但如果目标 Git 仓库已经存在，它将强制重置以使其类似于远程仓库的克隆。
> 是 `git-extras` 的一部分。
> 更多信息请访问：<https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>。

- 将 Git 仓库克隆到新目录中：

`git force-clone {{remote_repository_location}} {{path/to/directory}}`

- 将 Git 仓库克隆到新目录中，并检出特定分支：

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`

- 将 Git 仓库克隆到现有的 Git 仓库目录中，执行强制重置以使其类似于远程仓库，并检出特定分支：

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`