# git update-index

> 用于操作索引的 Git 命令。
> 更多信息：<https://git-scm.com/docs/git-update-index>。

- 假装一个已修改的文件没有改变（`git status` 不会将其显示为已更改）：

`git update-index --skip-worktree {{path/to/modified_file}}`