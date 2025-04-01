# git prune

> 从对象数据库中删除所有不可达对象的 Git 命令。
> 该命令通常不是直接使用，而是作为 Git gc 的内部命令。
> 更多信息：<https://git-scm.com/docs/git-prune>.

- 使用 Git prune 报告将被删除的对象，但不实际删除：

`git prune --dry-run`

- 删除不可达对象并显示已删除的对象到 `stdout`：

`git prune --verbose`

- 删除不可达对象的同时显示进度：

`git prune --progress`
