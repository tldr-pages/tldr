# safe

> 与 HashiCorp Vault 交互。
> 更多信息：<https://github.com/starkandwayne/safe>。

- 添加一个安全目标：

`safe target {{vault_addr}} {{target_name}}`

- 使用身份验证令牌对 Vault 服务器进行 CLI 客户端认证：

`safe auth {{authentication_token}}`

- 打印描述当前目标的环境变量：

`safe env`

- 显示给定路径的所有可访问密钥的树形层次结构：

`safe tree {{path}}`

- 将一个密钥从一个路径移动到另一个路径：

`safe move {{old/path/to/secret}} {{new/path/to/secret}}`

- 生成一个新的 2048 位 SSH 密钥对并存储：

`safe ssh {{2048}} {{path/to/secret}}`

- 为一个密钥设置非敏感键：

`safe set {{path/to/secret}} {{key}}={{value}}`

- 在密钥中设置自动生成的密码：

`safe gen {{path/to/secret}} {{key}}`