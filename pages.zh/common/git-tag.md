# git tag

> 创建、列出、删除或验证标签。
> 标签是对提交的静态引用。
> 更多信息：<https://git-scm.com/docs/git-tag>.

- 列出所有标签：

`git tag`

- 创建一个指向当前提交的标签：

`git tag {{tag_name}}`

- 创建一个指向指定提交的标签：

`git tag {{tag_name}} {{commit}}`

- 创建一个带有指定消息的注释标签：

`git tag {{tag_name}} {{[-m|--message]}} {{tag_message}}`

- 删除指定名称的标签：

`git tag {{[-d|--delete]}} {{tag_name}}`

- 从远程获取更新的标签：

`git fetch {{[-t|--tags]}}`

- 将标签推送到远程仓库：

`git push origin tag {{tag_name}}`

- 列出所有包含指定提交的祖先的标签：

`git tag --contains {{commit}}`