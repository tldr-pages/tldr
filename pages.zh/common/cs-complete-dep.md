# cs 完整依赖

> 搜索库而不直接在网络上进行。
> 更多信息：<https://get-coursier.io/docs/cli-complete>。

- 打印在特定 Maven 组标识符下发布的工件：

`cs complete-dep {{group_id}}`

- 列出在特定 Maven 组标识符和工件标识符下发布的库版本：

`cs complete-dep {{group_id}}:{{artifact_id}}`

- 打印在给定 Maven groupId 下发布的工件，搜索 ivy2local：

`cs complete-dep {{group_id}} --repository ivy2local`

- 列出在 Maven 组标识符下发布的工件，搜索特定的仓库和凭证：

`cs complete-dep {{group_id}}:{{artifact_id}} --repository {{repository_url}} --credentials {{user}}:{{password}}`