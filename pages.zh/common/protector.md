# protector

> 保护或取消保护 GitHub 仓库的分支。
> 更多信息：<https://github.com/jcgay/protector>.

- 保护 GitHub 仓库的分支（创建分支保护规则）：

`protector {{branches_regex}} -repos {{organization/repository}}`

- 使用 dry run 模式查看哪些分支将被保护（也可以用于取消保护）：

`protector -dry-run {{branches_regex}} -repos {{organization/repository}}`

- 取消保护 GitHub 仓库的分支（删除分支保护规则）：

`protector -free {{branches_regex}} -repos {{organization/repository}}`
