# gh

> 在命令行无缝使用 GitHub。
> 一些子命令（例如 `config`）有自己的使用文档。
> 更多信息：<https://cli.github.com/manual/gh>。

- 克隆一个 GitHub 仓库到本地：

`gh repo clone {{拥有者}}/{{仓库}}`

- 创建一个新 issue：

`gh issue {{[new|create]}}`

- 查看并筛选当前仓库中未解决的 issue：

`gh issue {{[ls|list]}}`

- 在默认浏览器中查看指定 issue：

`gh issue view {{[-w|--web]}} {{issue_号|url}}`

- 创建一个拉取请求：

`gh pr {{[new|create]}}`

- 在默认浏览器中查看拉取请求：

`gh pr view {{[-w|--web]}} {{pr_号|url|分支}}`

- 在本地检出指定的拉取请求：

`gh {{[co|pr checkout]}} {{pr_号|url|分支}}`

- 查看当前仓库中拉取请求的状态：

`gh pr status`
