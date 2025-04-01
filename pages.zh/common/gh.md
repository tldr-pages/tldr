# gh

> 与 GitHub 无缝协作。
> 一些子命令，如 `config`，有其自己的使用文档。
> 更多信息：<https://cli.github.com/>.

- 克隆 GitHub 仓库到本地：

`gh repo clone {{owner}}/{{repository}}`

- 创建一个新的问题：

`gh issue create`

- 查看并过滤当前仓库的开放问题：

`gh issue list`

- 在默认的网页浏览器中查看问题：

`gh issue view --web {{issue_number}}`

- 创建一个 Pull Request：

`gh pr create`

- 在默认的网页浏览器中查看 Pull Request：

`gh pr view --web {{pr_number}}`

- 本地签出特定的 Pull Request：

`gh pr checkout {{pr_number}}`

- 查看仓库 Pull Request 的状态：

`gh pr status`
