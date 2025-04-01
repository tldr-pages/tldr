# gh api

> 向 GitHub API 发送经过身份验证的 HTTP 请求并打印响应。
> 更多信息：<https://cli.github.com/manual/gh_api>.

- 以 JSON 格式显示当前仓库的发布版本：

`gh api repos/:owner/:repo/releases`

- 为特定问题创建一个反应：

`gh api --header {{Accept:application/vnd.github.squirrel-girl-preview+json}} --raw-field '{{content=+1}}' {{repos/:owner/:repo/issues/123/reactions}}`

- 以 JSON 格式显示 GraphQL 查询的结果：

`gh api graphql --field {{name=':repo'}} --raw-field '{{query}}'`

- 使用自定义 HTTP 方法发送请求：

`gh api --method {{POST}} {{endpoint}}`

- 在输出中包含 HTTP 响应头：

`gh api --include {{endpoint}}`

- 不打印响应体：

`gh api --silent {{endpoint}}`

- 向特定的 GitHub Enterprise Server 发送请求：

`gh api --hostname {{github.example.com}} {{endpoint}}`

- 显示子命令帮助：

`gh api --help`
