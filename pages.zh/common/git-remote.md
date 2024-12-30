# git remote

> 管理跟踪的仓库集（“远程”）。
> 更多信息：<https://git-scm.com/docs/git-remote>。

- 列出现有的远程及其名称和URL：

`git remote {{-v|--verbose}}`

- 显示远程的信息：

`git remote show {{remote_name}}`

- 添加一个远程：

`git remote add {{remote_name}} {{remote_url}}`

- 更改远程的URL（使用 `--add` 保留现有的URL）：

`git remote set-url {{remote_name}} {{new_url}}`

- 显示远程的URL：

`git remote get-url {{remote_name}}`

- 移除一个远程：

`git remote remove {{remote_name}}`

- 重命名一个远程：

`git remote rename {{old_name}} {{new_name}}`