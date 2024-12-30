# git utimes

> 将文件的修改时间更改为它们的最后提交日期。不会触及工作区或索引中的文件。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>。

- 将所有文件的修改时间更改为它们的最后提交日期：

`git utimes`

- 更改比其最后提交日期更新的文件的修改时间，保留从本地仓库提交的文件的原始修改时间：

`git utimes --newer`