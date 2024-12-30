# gh issue create

> 在一个仓库中创建 GitHub 问题。
> 更多信息：<https://cli.github.com/manual/gh_issue_create>。

- 以交互方式在当前仓库中创建一个新问题：

`gh issue create`

- 以交互方式创建一个带有 `bug` 标签的新问题：

`gh issue create --label "{{bug}}"`

- 以交互方式创建一个新问题并将其分配给指定用户：

`gh issue create --assignee {{user1,user2,...}}`

- 创建一个带有标题、正文并将其分配给当前用户的新问题：

`gh issue create --title "{{title}}" --body "{{body}}" --assignee "{{@me}}"`

- 以交互方式创建一个新问题，从文件中读取正文文本：

`gh issue create --body-file {{path/to/file}}`

- 在默认网页浏览器中创建一个新问题：

`gh issue create --web`

- 显示帮助信息：

`gh issue create --help`