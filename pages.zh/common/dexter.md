# dexter

> 使用 OpenId Connect 认证 `kubectl` 用户。
> 更多信息：<https://github.com/gini/dexter>.

- 使用 Google OIDC 创建并认证用户：

`dexter auth -i {{client_id}} -s {{client_secret}}`

- 覆盖默认的 kube 配置文件位置：

`dexter auth -i {{client_id}} -s {{client_secret}} --kube-config {{sample/config}}`
