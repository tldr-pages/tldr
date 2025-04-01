# git utimes

> 将文件的修改时间更改为最后一次提交的日期。不会影响工作树或索引中的文件。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>.

- 将所有文件的修改时间更改为最后一次提交的日期：

`git utimes`

- 将文件的修改时间更改为比最后一次提交日期新的时间，保留从本地仓库提交的文件的原始修改时间：

`git utimes --newer`