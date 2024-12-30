# doctl 应用

> 管理 DigitalOcean 应用。
> 更多信息：<https://docs.digitalocean.com/reference/doctl/reference/apps>。

- 创建一个应用：

`doctl apps create`

- 为特定应用创建一个部署：

`doctl apps create-deployment {{app_id}}`

- 交互式删除一个应用：

`doctl apps delete {{app_id}}`

- 获取一个应用：

`doctl apps get`

- 列出所有应用：

`doctl apps list`

- 列出特定应用的所有部署：

`doctl apps list-deployments {{app_id}}`

- 获取特定应用的日志：

`doctl apps logs {{app_id}}`

- 使用给定的应用规范更新特定应用：

`doctl apps update {{app_id}} --spec {{path/to/spec.yml}}`