# choco apikey

> 管理 Chocolatey 源的 API 密钥。
> 更多信息：<https://chocolatey.org/docs/commands-apikey>.

- 显示源及其 API 密钥的列表：

`choco apikey`

- 显示特定源及其 API 密钥：

`choco apikey --source "{{source_url}}"`

- 为源设置 API 密钥：

`choco apikey --source "{{source_url}}" --key "{{api_key}}"`

- 移除源的 API 密钥：

`choco apikey --source "{{source_url}}" --remove`
