# git show-branch

> 显示分支及其提交。
> 更多信息：<https://git-scm.com/docs/git-show-branch>。

- 显示某分支的最新提交摘要：

`git show-branch {{branch_name|ref|commit}}`

- 比较多个提交或分支的历史提交：

`git show-branch {{branch_name1|ref1|commit1 branch_name2|ref2|commit2 ...}}`

- 比较所有远程跟踪分支：

`git show-branch --remotes`

- 比较本地和远程跟踪分支：

`git show-branch --all`

- 列出所有分支的最新提交：

`git show-branch --all --list`

- 比较给定分支与当前分支：

`git show-branch --current {{commit|branch_name|ref}}`

- 显示完整的提交名称而非相对名称：

`git show-branch --sha1-name --current {{current|branch_name|ref}}`

- 超过共同祖先继续显示指定数量的提交：

`git show-branch --more {{5}} {{commit|branch_name|ref}} {{commit|branch_name|ref}} {{...}}`
