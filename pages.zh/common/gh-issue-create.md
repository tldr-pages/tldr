# gh issue create

> 在仓库中创建 GitHub 问题。
> 更多信息：<https://cli.github.com/manual/gh_issue_create>.

- 在当前仓库中交互式地创建新问题：

`gh issue create`

- 交互式地创建带有 `bug` 标签的新问题：

`gh issue create --label "{{bug}}"`

- 交互式地创建新问题并分配给指定用户：

`gh issue create --assignee {{user1,user2,...}}`

- 创建带有标题、正文并分配给当前用户的新问题：

`gh issue create --title "{{title}}" --body "{{body}}" --assignee "{{@me}}"`

- 交互式地创建新问题，从文件中读取正文内容：

`gh issue create --body-file {{path/to/file}}`

- 在默认的网络浏览器中创建新问题：

`gh issue create --web`

- 显示帮助：

`gh issue create --help`
