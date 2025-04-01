# git guilt

> 显示有未提交更改的文件的总归咎数量，或计算两个版本之间的归咎变化。
> `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-guilt>.

- 显示总归咎数量：

`git guilt`

- 计算两个版本之间的归咎变化：

`git guilt {{first_revision}} {{last_revision}}`

- 显示作者的电子邮件而不是姓名：

`git guilt --email`

- 归咎时忽略仅涉及空白的更改：

`git guilt --ignore-whitespace`

- 查找过去三周的归咎变化：

`git guilt 'git log --until="3 weeks ago" --format="%H" -n 1'`

- 查找过去三周的归咎变化（git 1.8.5+）：

`git guilt @{3.weeks.ago}`
