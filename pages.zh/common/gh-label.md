# gh 标签

> 与 GitHub 标签一起工作。
> 更多信息：<https://cli.github.com/manual/gh_label>。

- 列出当前目录中存储库的标签：

`gh label list`

- 在默认网页浏览器中查看当前目录中存储库的标签：

`gh label list --web`

- 为当前目录中存储库创建一个具有特定名称、描述和十六进制格式颜色的标签：

`gh label create {{name}} --description "{{description}}" --color {{color_hex}}`

- 删除当前目录中存储库的标签，并提示确认：

`gh label delete {{name}}`

- 更新当前目录中存储库的特定标签的名称和描述：

`gh label edit {{name}} --name {{new_name}} --description "{{description}}"`

- 从特定存储库克隆标签到当前目录中的存储库：

`gh label clone {{owner}}/{{repository}}`

- 显示子命令的帮助：

`gh label {{subcommand}} --help`