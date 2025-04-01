# git bisect

> 使用二分法查找引入错误的提交。
> Git 会自动在提交图中来回跳转，逐步缩小有错误的提交范围。
> 更多信息：<https://git-scm.com/docs/git-bisect>。

- 在一个已知有错误的提交和一个已知没有错误的提交（通常是较旧的）之间的提交范围内开始一个二分查找会话：

`git bisect start {{bad_commit}} {{good_commit}}`

- 对于 `git bisect` 选择的每个提交，在测试该提交是否存在该问题后，将其标记为“坏”或“好”：

`git bisect {{good|bad}}`

- 在 `git bisect` 找到有错误的提交后，结束二分查找会话并返回到之前的分支：

`git bisect reset`

- 在二分查找过程中跳过一个提交（例如，由于其他问题而导致测试失败的提交）：

`git bisect skip`

- 显示到目前为止已完成的操作日志：

`git bisect log`