# git submodule

> 检查、更新和管理子模块。
> 更多信息：<https://git-scm.com/docs/git-submodule>.

- 安装指定的子模块：

`git submodule update --init --recursive`

- 将 Git 仓库添加为子模块：

`git submodule add {{repository_url}}`

- 将 Git 仓库添加为指定目录下的子模块：

`git submodule add {{repository_url}} {{path/to/directory}}`

- 更新所有子模块到最新的提交：

`git submodule foreach git pull`
