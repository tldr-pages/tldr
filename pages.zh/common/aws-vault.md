# aws-vault

> 一个用于在开发环境中安全存储和访问 AWS 凭证的保险库。
> 更多信息：<https://github.com/99designs/aws-vault>.

- 将凭证添加到安全的密钥存储中：

`aws-vault add {{配置文件}}`

- 在环境中使用 AWS 凭证执行一个命令：

`aws-vault exec {{配置文件}} -- {{aws s3 ls}}`

- 打开浏览器窗口并登录到 AWS 控制台：

`aws-vault login {{配置文件}}`

- 列出配置文件，以及它们的凭证和会话：

`aws-vault list`

- 轮换 AWS 凭证：

`aws-vault rotate {{配置文件}}`

- 从安全的密钥存储中移除凭证：

`aws-vault remove {{配置文件}}`
