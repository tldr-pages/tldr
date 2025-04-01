# git cherry

> 找出尚未应用到上游的提交。
> 更多信息：<https://git-scm.com/docs/git-cherry>.

- 显示包含上游等效提交的提交（及其提交信息）：

`git cherry {{[-v|--verbose]}}`

- 指定不同的上游和主题分支：

`git cherry {{origin}} {{topic}}`

- 限制提交范围为给定基点内的提交：

`git cherry {{origin}} {{topic}} {{base}}`
