# gh issue create

> 创建 GitHub 仓库中的 issue。
> 更多信息：<https://cli.github.com/manual/gh_issue_create>。

- 以交互式方式在当前仓库中创建一个新 issue：

`gh issue {{[new|create]}}`

- 以交互式方式创建一个带有 "bug" 标签的新 issue：

`gh issue {{[new|create]}} {{[-l|--label]}} "bug"`

- 以交互式方式创建一个新 issue 并分配给指定的用户：

`gh issue {{[new|create]}} {{[-a|--assignee]}} {{用户1,用户2,...}}`

- 创建一个具有标题和描述的新 issue，并分配给当前用户：

`gh issue {{[new|create]}} {{[-t|--title]}} "{{标题}}" {{[-b|--body]}} "{{描述}}" {{[-a|--assignee]}} "@me"`

- 以交互式方式创建一个新 issue，并从文件中读取其描述正文：

`gh issue {{[new|create]}} {{[-F|--body-file]}} {{路径/到/文件}}`

- 在默认网页浏览器中创建一个新 issue：

`gh issue {{[new|create]}} {{[-w|--web]}}`

- 显示帮助：

`gh issue {{[new|create]}} {{[-h|--help]}}`
