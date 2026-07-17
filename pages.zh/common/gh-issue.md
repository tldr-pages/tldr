# gh issue

> 管理 GitHub issue。
> 更多信息：<https://cli.github.com/manual/gh_issue>。

- 显示指定的 issue：

`gh issue view {{issue_号}}`

- 在默认网页浏览器中查看指定的 issue：

`gh issue view {{issue_号}} {{[-w|--web]}}`

- 在默认网页浏览器中创建一个新 issue：

`gh issue {{[new|create]}} {{[-w|--web]}}`

- 列出最近 10 个带有 "bug" 标签的 issue：

`gh issue {{[ls|list]}} {{[-L|--limit]}} 10 {{[-l|--label]}} "bug"`

- 列出由指定用户创建的已关闭的 issue：

`gh issue {{[ls|list]}} {{[-s|--state]}} closed {{[-A|--author]}} {{用户名}}`

- 在指定仓库中，显示与当前用户相关的 issue 的状态：

`gh issue status {{[-R|--repo]}} {{拥有者}}/{{仓库}}`

- 重新打开指定的 issue：

`gh issue reopen {{issue_号}}`
