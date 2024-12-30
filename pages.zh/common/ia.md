# ia

> 命令行工具，用于与 `archive.org` 进行交互。
> 更多信息：<https://archive.org/services/docs/api/internetarchive/cli.html>。

- 使用 API 密钥配置 `ia`（某些功能在此步骤未完成时将无法使用）：

`ia configure`

- 上传一个或多个项目到 `archive.org`：

`ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"`

- 从 `archive.org` 下载一个或多个项目：

`ia download {{item}}`

- 从 `archive.org` 删除一个或多个项目：

`ia delete {{identifier}} {{file}}`

- 在 `archive.org` 上搜索，返回 JSON 格式的结果：

`ia search '{{subject:"subject" collection:collection}}'`