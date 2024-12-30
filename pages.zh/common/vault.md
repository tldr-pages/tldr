# vault

> 与 HashiCorp Vault 交互。
> 更多信息：<https://www.vaultproject.io/docs/commands>。

- 连接到 Vault 服务器并初始化一个新的加密数据存储：

`vault init`

- 通过提供访问加密数据存储所需的密钥共享之一来解封（解锁）保管库：

`vault unseal {{key-share-x}}`

- 使用身份验证令牌对 CLI 客户端进行身份验证，以便访问 Vault 服务器：

`vault auth {{authentication_token}}`

- 使用称为“secret”的通用后端在保管库中存储一个新秘密：

`vault write secret/{{hello}} value={{world}}`

- 使用称为“secret”的通用后端从保管库中读取一个值：

`vault read secret/{{hello}}`

- 从值中读取特定字段：

`vault read -field={{field_name}} secret/{{hello}}`

- 通过从内存中移除数据存储的加密密钥来封存（锁定）Vault 服务器：

`vault seal`