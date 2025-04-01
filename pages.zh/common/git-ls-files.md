# git ls-files

> 显示索引和工作树中文件的信息。
> 更多信息：<https://git-scm.com/docs/git-ls-files>。

- 显示已删除的文件：

`git ls-files --deleted`

- 显示已修改和已删除的文件：

`git ls-files --modified`

- 显示被忽略和未跟踪的文件：

`git ls-files --others`

- 显示未跟踪的文件，但不包括被忽略的文件：

`git ls-files --others --exclude-standard`
