# 安全

> 管理钥匙串、密钥、证书和安全框架。
> 更多信息：<https://keith.github.io/xcode-man-pages/security.1.html>。

- 列出所有可用的钥匙串：

`security list-keychains`

- 删除特定的钥匙串：

`security delete-keychain {{path/to/file.keychain}}`

- 创建一个钥匙串：

`security create-keychain -p {{密码}} {{path/to/file.keychain}}`

- 根据网站或服务的公共名称设置证书（如果存在多个具有相同公共名称的证书，则会失败）：

`security set-identity-preference -s {{URL|主机名|服务}} -c "{{公共名称}}" {{path/to/file.keychain}}`

- 从文件向钥匙串中添加证书（如果未指定 -k，则使用默认钥匙串）：

`security add-certificates -k {{file.keychain}} {{path/to/cert_file.pem}}`

- 将 CA 证书添加到每用户信任设置中：

`security add-trusted-cert -k {{path/to/user-keychain.keychain-db}} {{path/to/ca-cert_file.pem}}`

- 从每用户信任设置中移除 CA 证书：

`security remove-trusted-cert {{path/to/ca-cert_file.pem}}`