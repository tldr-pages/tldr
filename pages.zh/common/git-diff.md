# git diff

> 显示已跟踪文件的内容变更。
> 更多信息：<https://git-scm.com/docs/git-diff>.

- 显示未暂存的更改：

`git diff`

- 显示所有未提交的更改（包括已暂存的）：

`git diff HEAD`

- 仅显示已暂存（添加过但未提交）的更改：

`git diff --staged`

- 显示过去某段时间内所有提交的变更（日期表达式如“1 week 2 days”或 ISO 日期）：

`git diff 'HEAD@{{{3 months|weeks|days|hours|seconds ago}}}'`

- 显示差异统计信息（如文件变更列表、直方图及总行数增删）：

`git diff --stat {{提交}}`

- 输出自某次提交以来的文件创建、重命名及权限变更的摘要：

`git diff --summary {{提交}}`

- 比较两个分支或提交之间的单个文件：

`git diff {{分支1}}..{{分支2}} {{路径/到/文件}}`

- 将当前分支的某文件与其他分支的对应文件进行对比：

`git diff {{分支}}:{{路径/到/文件2}} {{路径/到/文件}}`
