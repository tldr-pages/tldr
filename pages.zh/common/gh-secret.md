# gh secret

> 管理 GitHub 秘钥。
> 更多信息：<https://cli.github.com/manual/gh_secret>.

- 列出当前仓库的秘钥：

`gh secret list`

- 列出特定组织的秘钥：

`gh secret list --org {{organization}}`

- 列出特定仓库的秘钥：

`gh secret list --repo {{owner}}/{{repository}}`

- 为当前仓库设置秘钥（用户将被提示输入值）：

`gh secret set {{name}}`

- 从文件中为当前仓库设置秘钥：

`gh secret set {{name}} < {{path/to/file}}`

- 为特定仓库设置组织秘钥：

`gh secret set {{name}} --org {{organization}} --repos {{repository1,repository2}}`

- 删除当前仓库的秘钥：

`gh secret remove {{name}}`

- 删除特定组织的秘钥：

`gh secret remove {{name}} --org {{organization}}`