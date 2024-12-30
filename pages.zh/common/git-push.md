# git push

> 将提交推送到远程仓库。
> 更多信息：<https://git-scm.com/docs/git-push>。

- 将当前分支的本地更改发送到其默认的远程对应分支：

`git push`

- 将特定本地分支的更改发送到其远程对应分支：

`git push {{remote_name}} {{local_branch}}`

- 将特定本地分支的更改发送到其远程对应分支，并将远程分支设置为本地分支的默认推送/拉取目标：

`git push -u {{remote_name}} {{local_branch}}`

- 将特定本地分支的更改发送到特定远程分支：

`git push {{remote_name}} {{local_branch}}:{{remote_branch}}`

- 将所有本地分支的更改发送到给定远程仓库中的对应分支：

`git push --all {{remote_name}}`

- 删除远程仓库中的一个分支：

`git push {{remote_name}} --delete {{remote_branch}}`

- 移除没有本地对应分支的远程分支：

`git push --prune {{remote_name}}`

- 发布尚未在远程仓库中的标签：

`git push --tags`