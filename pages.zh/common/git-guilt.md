# git guilt

> 显示未暂存更改的文件的总责任计数，或计算两个修订之间的责任变化。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-guilt>。

- 显示总责任计数：

`git guilt`

- 计算两个修订之间的责任变化：

`git guilt {{first_revision}} {{last_revision}}`

- 显示作者的电子邮件而不是名字：

`git guilt --email`

- 在归属责任时忽略仅有空格的更改：

`git guilt --ignore-whitespace`

- 查找过去三周的责任增量：

`git guilt 'git log --until="3 weeks ago" --format="%H" -n 1'`

- 查找过去三周的责任增量（git 1.8.5+）：

`git guilt @{3.weeks.ago}`