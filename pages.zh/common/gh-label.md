# gh label

> 管理 GitHub 标签。
> 更多信息：<https://cli.github.com/manual/gh_label>.

- 列出当前目录中仓库的标签：

`gh label list`

- 在默认的网页浏览器中查看当前目录中仓库的标签：

`gh label list --web`

- 为当前目录中的仓库创建具有特定名称、描述和十六进制颜色的标签：

`gh label create {{name}} --description "{{description}}" --color {{color_hex}}`

- 删除当前目录中仓库的一个标签，删除前会提示确认：

`gh label delete {{name}}`

- 更新当前目录中仓库的特定标签的名称和描述：

`gh label edit {{name}} --name {{new_name}} --description "{{description}}"`

- 从特定仓库复制标签到当前目录中的仓库：

`gh label clone {{owner}}/{{repository}}`

- 显示子命令的帮助信息：

`gh label {{subcommand}} --help`