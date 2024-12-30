# git range-diff

> 比较两个提交范围（例如，分支的两个版本）。
> 更多信息：<https://git-scm.com/docs/git-range-diff>。

- 对两个单独提交的更改进行差异比较：

`git range-diff {{commit_1}}^! {{commit_2}}^!`

- 从它们的共同祖先对我们的和他们的更改进行差异比较，例如在交互式变基之后：

`git range-diff {{theirs}}...{{ours}}`

- 对两个提交范围的更改进行差异比较，例如检查在从 `base1` 变基到 `base2` 时冲突是否已适当地解决：

`git range-diff {{base1}}..{{rev1}} {{base2}}..{{rev2}}`