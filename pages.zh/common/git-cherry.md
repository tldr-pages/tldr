# git cherry

> 查找尚未应用到上游的提交。
> 更多信息：<https://git-scm.com/docs/git-cherry>。

- 显示与上游具有相同提交（及其信息）的提交：

`git cherry {{-v|--verbose}}`

- 指定不同的上游和主题分支：

`git cherry {{origin}} {{topic}}`

- 将提交限制在给定限制内：

`git cherry {{origin}} {{topic}} {{base}}`