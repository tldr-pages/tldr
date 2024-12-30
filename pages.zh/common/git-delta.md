# git delta

> 列出与另一个分支不同的文件。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-delta>。

- 列出与 `main` 分支不同的当前检出的分支的文件：

`git delta {{main}}`

- 列出与另一个特定分支不同的特定分支的文件：

`git delta {{branch_1}} {{branch_2}}`