# git reset

> 通过将当前 Git HEAD 重置为指定状态来撤销提交或取消暂存更改。
> 如果传递的是路径，则它的作用是“取消暂存”；如果传递的是提交哈希或分支，则它的作用是“撤销提交”。
> 更多信息：<https://git-scm.com/docs/git-reset>。

- 取消暂存所有内容：

`git reset`

- 取消暂存特定文件：

`git reset {{path/to/file1 path/to/file2 ...}}`

- 交互式取消暂存文件的部分内容：

`git reset --patch {{path/to/file}}`

- 撤销上一个提交，同时保留其更改（以及文件系统中任何未提交的更改）：

`git reset HEAD~`

- 撤销最后两个提交，将其更改添加到索引中，即暂存以便提交：

`git reset --soft HEAD~2`

- 丢弃任何未提交的更改，无论是否已暂存（仅对未暂存的更改，请使用 `git checkout`）：

`git reset --hard`

- 将仓库重置为给定的提交，丢弃自那时以来的已提交、已暂存和未提交的更改：

`git reset --hard {{commit}}`