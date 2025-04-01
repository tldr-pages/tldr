# git summary

> 显示 Git 仓库的信息。
> `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>。

- 显示 Git 仓库的数据：

`git summary`

- 从某个提交、分支或标签开始显示 Git 仓库的数据：

`git summary {{commit|分支名|标签名}}`

- 显示 Git 仓库的数据，合并使用不同电子邮件的提交者，为每个作者提供一个统计：

`git summary --dedup-by-email`

- 显示 Git 仓库的数据，显示每个贡献者修改的行数：

`git summary --line`
