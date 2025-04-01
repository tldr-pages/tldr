# git update-index

> 用于操作 Git 索引的命令。
> 更多信息：<https://git-scm.com/docs/git-update-index>。

- 假装某个已修改的文件未被修改（`git status` 不会显示此文件已更改）：

`git update-index --skip-worktree {{path/to/modified_file}}`