# gh secret set

> 创建或更新 GitHub 秘密。
> 更多信息：<https://cli.github.com/manual/gh_secret_set>。

- 为当前仓库设置一个秘密（用户将被提示输入值）：

`gh secret set {{name}}`

- 从文件为当前仓库设置一个秘密：

`gh secret set {{name}} < {{path/to/file}}`

- 为特定仓库设置一个秘密：

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- 为特定仓库设置组织秘密：

`gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"`

- 设置具有特定可见性的组织秘密：

`gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}`