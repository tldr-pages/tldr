# hub

> Git 的封装，用于增强 GitHub 项目的操作。
> 根据 `hub alias` 的说明进行设置后，可以使用 `git` 命令来运行 `hub` 命令。
> 更多信息：<https://hub.github.com>.

- 使用仓库的简短名称（所有者可以省略用户名）克隆仓库：

`hub clone {{username}}/{{repo_name}}`

- 在你自己的 GitHub 账号下创建当前仓库（从其他用户克隆）的分支：

`hub fork`

- 将当前本地分支推送到 GitHub 并在原仓库中创建一个合并请求：

`hub push {{remote_name}} && hub pull-request`

- 为当前（已推送的）分支创建一个合并请求，并重用首次提交的提交信息：

`hub pull-request --no-edit`

- 从合并请求的内容创建新分支并切换到该分支：

`hub pr checkout {{pr_number}}`

- 将当前（仅本地）仓库上传到你的 GitHub 账号：

`hub create`

- 从上游获取 Git 对象并更新本地分支：

`hub sync`