# git merge-base

> 查找两个提交的共同祖先。
> 更多信息：<https://git-scm.com/docs/git-merge-base>。

- 打印两个提交的最佳共同祖先：

`git merge-base {{commit_1}} {{commit_2}}`

- 打印两个提交的所有最佳共同祖先：

`git merge-base --all {{commit_1}} {{commit_2}}`

- 检查一个提交是否是特定提交的祖先：

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
