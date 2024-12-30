# git fetch

> 从远程仓库下载对象和引用。
> 更多信息：<https://git-scm.com/docs/git-fetch>。

- 从默认的远程上游仓库（如果设置了）获取最新更改：

`git fetch`

- 从特定的远程上游仓库获取新分支：

`git fetch {{remote_name}}`

- 从所有远程上游仓库获取最新更改：

`git fetch --all`

- 还从远程上游仓库获取标签：

`git fetch --tags`

- 删除对已在上游删除的远程分支的本地引用：

`git fetch --prune`