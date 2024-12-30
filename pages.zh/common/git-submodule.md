# git 子模块

> 检查、更新和管理子模块。
> 更多信息：<https://git-scm.com/docs/git-submodule>。

- 安装一个仓库的指定子模块：

`git submodule update --init --recursive`

- 将一个 Git 仓库作为子模块添加：

`git submodule add {{repository_url}}`

- 将一个 Git 仓库作为子模块添加到指定目录：

`git submodule add {{repository_url}} {{path/to/directory}}`

- 更新每个子模块到其最新提交：

`git submodule foreach git pull`