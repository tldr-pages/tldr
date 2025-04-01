# git ls-remote

> 列出远程仓库中的引用（基于名称或 URL）。
> 如果没有提供名称或 URL，则使用配置的上游分支，如果上游分支未配置，则使用远程仓库 origin。
> 更多信息：<https://git-scm.com/docs/git-ls-remote>.

- 显示默认远程仓库中的所有引用：

`git ls-remote`

- 显示默认远程仓库中的所有分支引用：

`git ls-remote --heads`

- 显示默认远程仓库中的所有标签引用：

`git ls-remote --tags`

- 显示基于名称或 URL 的远程仓库中的所有引用：

`git ls-remote {{repository_url}}`

- 显示远程仓库中符合某种模式的引用：

`git ls-remote {{repository_name}} "{{pattern}}"`