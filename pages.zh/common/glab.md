# glab

> 与 GitLab 无缝协作。
> 某些子命令（如 `config`）有自己的使用文档。
> 更多信息：<https://github.com/profclems/glab>。

- 克隆 GitLab 仓库到本地：

`glab repo clone {{owner}}/{{repository}}`

- 创建一个新问题：

`glab issue create`

- 查看并过滤当前仓库的未解决问题：

`glab issue list`

- 在默认浏览器中查看问题：

`glab issue view --web {{issue_number}}`

- 创建一个合并请求：

`glab mr create`

- 在默认网页浏览器中查看一个拉取请求：

`glab mr view --web {{pr_number}}`

- 在本地签出特定的拉取请求：

`glab mr checkout {{pr_number}}`