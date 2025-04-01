# git stash

> 将本地 Git 更改存放在临时区域。
> 更多信息：<https://git-scm.com/docs/git-stash>。

- 将当前更改（不包括新文件）存入stash，并附带消息：

`git stash push {{[-m|--message]}} {{可选的stash消息}}`

- 将当前更改，包括新文件（未跟踪文件）存入stash：

`git stash {{[-u|--include-untracked]}}`

- 交互式选择更改文件的部分内容存入stash：

`git stash {{[-p|--patch]}}`

- 列出所有 stash（显示 stash 名称、相关分支和消息）：

`git stash list`

- 显示 stash 与最初创建 stash 时的提交之间的更改（默认为 `stash@{0}`）：

`git stash show {{[-p|--patch]}} {{stash@{0}}}`

- 应用 stash（默认为最新的 stash@{0}）：

`git stash apply {{可选的stash名称或提交}}`

- 应用并删除 stash（默认为 stash@{0}，如果应用时不引起冲突）：

`git stash pop {{可选的stash名称}}`

- 删除所有 stash：

`git stash clear`
