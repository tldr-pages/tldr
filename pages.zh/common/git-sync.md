# git sync

> 同步本地分支与远程分支。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>。

- 同步当前本地分支与其远程分支：

`git sync`

- 同步当前本地分支与远程主分支：

`git sync origin main`

- 同步时不清理未跟踪的文件：

`git sync -s {{remote_name}} {{branch_name}}`