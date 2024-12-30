# git shortlog

> 总结 `git log` 输出。
> 更多信息：<https://git-scm.com/docs/git-shortlog>。

- 查看所有提交的摘要，按作者姓名字母顺序分组：

`git shortlog`

- 查看所有提交的摘要，按提交次数排序：

`git shortlog {{-n|--numbered}}`

- 查看所有提交的摘要，按提交者身份（姓名和电子邮件）分组：

`git shortlog {{-c|--committer}}`

- 查看最近 5 次提交的摘要（即指定修订范围）：

`git shortlog HEAD~5..HEAD`

- 查看当前分支中所有用户、电子邮件和提交次数：

`git shortlog {{-s|--summary}} {{-n|--numbered}} {{-e|--email}}`

- 查看所有分支中所有用户、电子邮件和提交次数：

`git shortlog {{-s|--summary}} {{-n|--numbered}} {{-e|--email}} --all`