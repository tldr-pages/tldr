# git 同步

> 将本地分支与远程分支同步。
> 属于 `git-extras` 的一部分。
> 更多信息请访问：<https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>。

- 将当前本地分支与其远程分支同步：

`git sync`

- 将当前本地分支与远程主分支同步：

`git sync origin main`

- 在不清理未跟踪文件的情况下同步：

`git sync -s {{remote_name}} {{branch_name}}`