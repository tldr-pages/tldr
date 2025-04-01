# cs complete-dep

> 在不直接使用网页的情况下搜索库。
> 更多信息：<https://get-coursier.io/docs/cli-complete>。

- 打印特定 Maven 组标识符下发布的工件：

`cs complete-dep {{group_id}}`

- 列出特定 Maven 组标识符和工件标识符下发布的库版本：

`cs complete-dep {{group_id}}:{{artifact_id}}`

- 在 ivy2local 中搜索给定的 Maven 组 ID 下发布的工件：

`cs complete-dep {{group_id}} --repository ivy2local`

- 在特定仓库和凭据中搜索特定 Maven 组标识符下发布的工件：

`cs complete-dep {{group_id}}:{{artifact_id}} --repository {{repository_url}} --credentials {{user}}:{{password}}`