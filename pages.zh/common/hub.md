# hub

> 一个为 Git 提供的包装器，增加了用于处理基于 GitHub 项目的命令。
> 如果按照 `hub alias` 的说明进行设置，可以使用 `git` 来运行 `hub` 命令。
> 更多信息：<https://hub.github.com>。

- 使用其简写克隆一个仓库（所有者可以省略用户名）：

`hub clone {{username}}/{{repo_name}}`

- 在你的 GitHub 个人资料下创建当前仓库（从其他用户克隆）的一个分叉：

`hub fork`

- 将当前本地分支推送到 GitHub，并为其在原始仓库中创建一个 PR：

`hub push {{remote_name}} && hub pull-request`

- 创建当前（已推送）分支的 PR，重用第一个提交的消息：

`hub pull-request --no-edit`

- 使用拉取请求的内容创建一个新分支并切换到该分支：

`hub pr checkout {{pr_number}}`

- 将当前（仅本地）仓库上传到你的 GitHub 账户：

`hub create`

- 从上游获取 Git 对象并更新本地分支：

`hub sync`