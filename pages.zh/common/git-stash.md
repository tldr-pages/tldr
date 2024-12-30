# git stash

> 将本地 Git 更改存储在临时区域。
> 更多信息: <https://git-scm.com/docs/git-stash>。

- 使用 [m] 消息存储当前更改，但不包括新（未跟踪）文件：

`git stash push --message {{optional_stash_message}}`

- 存储当前更改，包括新（[u] 未跟踪）文件：

`git stash --include-untracked`

- 交互式选择要存储的已更改文件的 [p] 部分：

`git stash --patch`

- 列出所有存储（显示存储名称、相关分支和消息）：

`git stash list`

- 显示存储（默认是 `stash@{0}`）和存储条目首次创建时的提交之间的更改作为 [p] 补丁：

`git stash show --patch {{stash@{0}}}`

- 应用一个存储（默认是最新的，命名为 stash@{0}）：

`git stash apply {{optional_stash_name_or_commit}}`

- 弹出或应用一个存储（默认是 stash@{0}），如果应用不引起冲突，则将其从存储列表中移除：

`git stash pop {{optional_stash_name}}`

- 删除所有存储：

`git stash clear`