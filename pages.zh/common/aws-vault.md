# aws-vault

> 一个用于在开发环境中安全存储和访问 AWS 凭证的保险库。
> 更多信息：<https://github.com/99designs/aws-vault>。

- 将凭证添加到安全密钥库：

`aws-vault add {{profile}}`

- 在环境中使用 AWS 凭证执行命令：

`aws-vault exec {{profile}} -- {{aws s3 ls}}`

- 打开浏览器窗口并登录到 AWS 控制台：

`aws-vault login {{profile}}`

- 列出配置文件及其凭证和会话：

`aws-vault list`

- 轮换 AWS 凭证：

`aws-vault rotate {{profile}}`

- 从安全密钥库中移除凭证：

`aws-vault remove {{profile}}`