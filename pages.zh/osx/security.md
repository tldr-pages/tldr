# security

> 管理 keychains、密钥、证书和 Security 框架。
> 更多信息：<https://keith.github.io/xcode-man-pages/security.1.html>.

- 列出所有可用的 keychain：

`security list-keychains`

- 删除特定的 keychain：

`security delete-keychain {{path/to/file.keychain}}`

- 创建一个 keychain：

`security create-keychain -p {{password}} {{path/to/file.keychain}}`

- 通过证书的通用名称设置证书以用于网站或服务（如果存在多个具有相同通用名称的证书，将失败）：

`security set-identity-preference -s {{URL|hostname|service}} -c "{{common_name}}" {{path/to/file.keychain}}`

- 从文件中添加证书到 keychain（如果未指定 -k，则使用默认 keychain）：

`security add-certificates -k {{file.keychain}} {{path/to/cert_file.pem}}`

- 添加 CA 证书到每个用户的信任设置：

`security add-trusted-cert -k {{path/to/user-keychain.keychain-db}} {{path/to/ca-cert_file.pem}}`

- 从每个用户的信任设置中移除 CA 证书：

`security remove-trusted-cert {{path/to/ca-cert_file.pem}}`