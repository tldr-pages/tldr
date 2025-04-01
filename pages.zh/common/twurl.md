# twurl

> 类似于 curl 的命令，但专门为 Twitter API 定制。
> 更多信息：<https://github.com/twitter/twurl>。

- 授权 `twurl` 访问 Twitter 账户：

`twurl authorize --consumer-key {{twitter_api_key}} --consumer-secret {{twitter_api_secret}}`

- 向 API 端点发送 GET 请求：

`twurl -X GET {{twitter_api_endpoint}}`

- 向 API 端点发送 POST 请求：

`twurl -X POST -d '{{endpoint_params}}' {{twitter_api_endpoint}}`

- 上传媒体到 Twitter：

`twurl -H "{{twitter_upload_url}}" -X POST "{{twitter_upload_endpoint}}" --file "{{path/to/media.jpg}}" --file-field "media"`

- 访问不同的 Twitter API 主机：

`twurl -H {{twitter_api_url}} -X GET {{twitter_api_endpoint}}`

- 为请求的资源创建别名：

`twurl alias {{alias_name}} {{resource}}`
