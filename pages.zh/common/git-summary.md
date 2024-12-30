# git 概要

> 显示有关 Git 仓库的信息。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>。

- 显示有关 Git 仓库的数据：

`git summary`

- 显示自某次提交以来的 Git 仓库数据：

`git summary {{commit|branch_name|tag_name}}`

- 显示有关 Git 仓库的数据，将使用不同电子邮件的提交者合并为每位作者的 1 个统计数据：

`git summary --dedup-by-email`

- 显示有关 Git 仓库的数据，显示每位贡献者修改的行数：

`git summary --line`