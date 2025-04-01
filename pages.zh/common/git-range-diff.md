# git range-diff

> 比较两个提交范围（例如两个分支的版本）。
> 更多信息：<https://git-scm.com/docs/git-range-diff>。

- 比较两个单独提交的更改：

`git range-diff {{commit_1}}^! {{commit_2}}^!`

- 从共同祖先比较我们和他们之间的更改，例如在交互式变基之后：

`git range-diff {{theirs}}...{{ours}}`

- 比较两个提交范围的更改，例如检查从 `base1` 变基到 `base2` 的提交时是否正确解决了冲突：

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`