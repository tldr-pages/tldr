# git prune

> Git 命令用于从对象数据库中修剪所有不可达对象。
> 该命令通常不是直接使用，而是作为 Git gc 使用的内部命令。
> 更多信息：<https://git-scm.com/docs/git-prune>。

- 报告 Git prune 将移除的内容，但不实际移除：

`git prune --dry-run`

- 修剪不可达对象并将修剪内容显示到 `stdout`：

`git prune --verbose`

- 修剪不可达对象并显示进度：

`git prune --progress`