# git shortlog

> 汇总 `git log` 的输出。
> 更多信息：<https://git-scm.com/docs/git-shortlog>.

- 查看按作者姓名字母顺序分组的所有提交的摘要：

`git shortlog`

- 查看按提交数量排序的所有提交的摘要：

`git shortlog {{[-n|--numbered]}}`

- 查看按提交者身份（姓名和邮箱）分组的所有提交的摘要：

`git shortlog {{[-c|--committer]}}`

- 查看最近 5 次提交的摘要（即指定修订范围）：

`git shortlog HEAD~5..HEAD`

- 查看当前分支中的所有用户、邮箱和提交数量：

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}}`

- 查看所有分支中的所有用户、邮箱和提交数量：

`git shortlog {{[-s|--summary]}} {{[-n|--numbered]}} {{[-e|--email]}} --all`