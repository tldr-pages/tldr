# git diff

> 显示被跟踪文件的更改。
> 更多信息：<https://git-scm.com/docs/git-diff>。

- 显示未暂存的更改：

`git diff`

- 显示所有未提交的更改（包括已暂存的）：

`git diff HEAD`

- 仅显示已暂存（已添加但尚未提交）的更改：

`git diff --staged`

- 显示自给定日期/时间以来所有提交的更改（日期表达式，例如“1周2天”或ISO日期）：

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- 显示差异统计信息，如更改的文件、直方图和总行插入/删除数：

`git diff --stat {{commit}}`

- 输出自给定提交以来文件创建、重命名和模式更改的摘要：

`git diff --summary {{commit}}`

- 比较两个分支或提交之间的单个文件：

`git diff {{branch_1}}..{{branch_2}} [--] {{path/to/file}}`

- 将当前分支的不同文件与其他分支进行比较：

`git diff {{branch}}:{{path/to/file2}} {{path/to/file}}`