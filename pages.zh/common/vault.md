# vault

> 与 HashiCorp Vault 交互。
> 更多信息：<https://www.vaultproject.io/docs/commands>.

- 连接到 Vault 服务器并初始化一个新的加密数据存储：

`vault init`

- 使用所需的密钥份额之一解锁 Vault：

`vault unseal {{key-share-x}}`

- 使用身份验证令牌对 CLI 客户端进行身份验证：

`vault auth {{authentication_token}}`

- 使用名为 "secret" 的通用后端在 Vault 中存储一个新秘密：

`vault write secret/{{hello}} value={{world}}`

- 使用名为 "secret" 的通用后端从 Vault 中读取一个值：

`vault read secret/{{hello}}`

- 从值中读取特定字段：

`vault read -field={{field_name}} secret/{{hello}}`

- 通过从内存中移除数据存储的加密密钥来锁定 Vault 服务器：

`vault seal`
