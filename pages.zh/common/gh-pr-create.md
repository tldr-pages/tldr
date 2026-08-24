# gh pr create

> 管理 GitHub 拉取请求。
> 更多信息：<https://cli.github.com/manual/gh_pr_create>。

- 以交互式方式创建一个拉取请求：

`gh pr {{[new|create]}}`

- 创建一个拉取请求，并根据当前分支的提交记录自动填充标题和描述：

`gh pr {{[new|create]}} {{[-f|--fill]}}`

- 创建一个草稿拉取请求：

`gh pr {{[new|create]}} {{[-d|--draft]}}`

- 创建一个拉取请求并指定目标分支、标题和描述：

`gh pr {{[new|create]}} {{[-B|--base]}} {{目标分支}} {{[-t|--title]}} "{{标题}}" {{[-b|--body]}} "{{描述}}"`

- 在默认网页浏览器中打开以创建拉取请求：

`gh pr {{[new|create]}} {{[-w|--web]}}`
