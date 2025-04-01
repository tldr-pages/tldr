# ia

> 与 `archive.org` 交互的命令行工具。
> 更多信息：<https://archive.org/services/docs/api/internetarchive/cli.html>.

- 使用 API 密钥配置 `ia`（某些功能没有这一步无法工作）：

`ia configure`

- 上传一个或多个文件到 `archive.org`：

`ia upload {{identifier}} {{path/to/file}} --metadata="{{mediatype:data}}" --metadata="{{title:example}}"`

- 从 `archive.org` 下载一个或多个项目：

`ia download {{item}}`

- 从 `archive.org` 删除一个或多个项目：

`ia delete {{identifier}} {{file}}`

- 在 `archive.org` 上搜索，返回结果为 JSON 格式：

`ia search '{{subject:"subject" collection:collection}}'`