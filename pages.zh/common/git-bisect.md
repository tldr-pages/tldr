# git bisect

> 使用二分查找定位引入错误的提交。
> Git 会自动在提交历史中来回跳转，逐步缩小问题提交的范围。
> 更多信息：<https://git-scm.com/docs/git-bisect>.

- 在已知有问题提交和已知正常提交（通常较旧）之间开始二分查找会话：

`git bisect start {{问题提交}} {{正常提交}}`

- 对 `git bisect` 自动选中的每个提交进行测试后，标记为"正常"或"有问题"：

`git bisect {{good|bad}}`

- 当 `git bisect` 定位到问题提交后，结束二分查找会话并返回原分支：

`git bisect reset`

- 在二分查找过程中跳过某个提交（例如因其他问题导致测试失败的提交）：

`git bisect skip`

- 显示当前二分查找的进度日志：

`git bisect log`
