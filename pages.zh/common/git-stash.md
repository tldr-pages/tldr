# git stash

> 将本地 Git 更改临时保存到贮藏区。
> 更多信息：<https://git-scm.com/docs/git-stash>。

- 贮藏当前未提交的更改：

`git stash`

- 贮藏当前更改，包括新建的未跟踪文件：

`git stash {{[-u|--include-untracked]}}`

- 交互式选择要贮藏的更改片段：

`git stash {{[-p|--patch]}}`

- 列出所有贮藏条目：

`git stash list`

- 以补丁形式显示贮藏内容与贮藏时的提交之间的差异：

`git stash show {{[-p|--patch]}}`

- 应用贮藏条目，若没有冲突则从列表中移除该条目：

`git stash pop`

- 删除最新的贮藏条目：

`git stash drop`

- 删除所有贮藏条目：

`git stash clear`
