# gh secret set

> 创建或更新 GitHub 机密。
> 更多信息：<https://cli.github.com/manual/gh_secret_set>.

- 为当前仓库设置机密（用户将被提示输入值）：

`gh secret set {{name}}`

- 从文件为当前仓库设置机密：

`gh secret set {{name}} < {{path/to/file}}`

- 为特定仓库设置机密：

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- 为特定仓库设置组织机密：

`gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"`

- 以特定可见性设置组织机密：

`gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}`