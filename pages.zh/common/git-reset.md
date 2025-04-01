# git reset

> 撤销提交或取消暂存更改，通过重置当前 Git HEAD 到指定状态。
> 如果传递路径，则作为“取消暂存”；如果传递提交哈希或分支，则作为“撤销提交”。
> 更多信息：<https://git-scm.com/docs/git-reset>.

- 取消暂存所有更改：

`git reset`

- 取消暂存特定文件：

`git reset {{path/to/file1 path/to/file2 ...}}`

- 交互式取消暂存文件的部分内容：

`git reset --patch {{path/to/file}}`

- 撤销最后一次提交，保留其更改（以及任何其他未提交的更改）在文件系统中：

`git reset HEAD~`

- 撤销最后两次提交，将其更改添加到索引，即暂存用于提交：

`git reset --soft HEAD~2`

- 丢弃所有未提交的更改，无论是否已暂存（仅对未暂存的更改，使用 `git checkout`）：

`git reset --hard`

- 将仓库重置到指定的提交，丢弃自那时以来的已提交、已暂存和未提交的更改：

`git reset --hard {{commit}}`