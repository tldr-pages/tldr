# git bisect

> 使用二分查找来找到引入错误的提交。
> Git 会自动在提交图中前后跳转，逐步缩小故障提交的范围。
> 更多信息请访问: <https://git-scm.com/docs/git-bisect>。

- 在一个已知有缺陷的提交和一个已知正常（通常是较旧的）提交之间启动 bisect 会话：

`git bisect start {{bad_commit}} {{good_commit}}`

- 对于 `git bisect` 选择的每个提交，在测试完该问题后，将其标记为“坏”或“好”：

`git bisect {{good|bad}}`

- 在 `git bisect` 确定故障提交后，结束 bisect 会话并返回到之前的分支：

`git bisect reset`

- 在 bisect 过程中跳过某个提交（例如，由于其他问题而测试失败的提交）：

`git bisect skip`

- 显示到目前为止所做操作的日志：

`git bisect log`