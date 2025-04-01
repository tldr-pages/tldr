# git fetch

> 从远程仓库下载对象和引用。
> 更多信息：<https://git-scm.com/docs/git-fetch>.

- 从默认的远程上游仓库（如果已设置）拉取最新更改：

`git fetch`

- 从特定的远程上游仓库拉取新分支：

`git fetch {{remote_name}}`

- 从所有远程上游仓库拉取最新更改：

`git fetch --all`

- 同时从远程上游仓库拉取标签：

`git fetch --tags`

- 删除对远程已删除分支的本地引用：

`git fetch --prune`