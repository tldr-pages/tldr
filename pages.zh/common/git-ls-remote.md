# git ls-remote

> Git 命令，用于列出基于名称或 URL 的远程仓库中的引用。
> 如果未提供名称或 URL，则将使用配置的上游分支，如果未配置上游分支，则将使用远程 origin。
> 更多信息：<https://git-scm.com/docs/git-ls-remote>。

- 显示默认远程仓库中的所有引用：

`git ls-remote`

- 仅显示默认远程仓库中的头引用：

`git ls-remote --heads`

- 仅显示默认远程仓库中的标签引用：

`git ls-remote --tags`

- 根据名称或 URL 显示远程仓库中的所有引用：

`git ls-remote {{repository_url}}`

- 根据模式过滤显示远程仓库中的引用：

`git ls-remote {{repository_name}} "{{pattern}}"`