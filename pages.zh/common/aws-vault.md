# aws-vault

> 在开发环境中安全地存储和访问 AWS 凭据的工具。
> 更多信息：<https://github.com/99designs/aws-vault>.

- 将凭据添加到安全密钥库：

`aws-vault add {{profile}}`

- 使用环境中的 AWS 凭据执行命令：

`aws-vault exec {{profile}} -- {{aws s3 ls}}`

- 打开浏览器窗口并登录到 AWS 控制台：

`aws-vault login {{profile}}`

- 列出配置文件及其凭据和会话：

`aws-vault list`

- 旋转 AWS 凭据：

`aws-vault rotate {{profile}}`

- 从安全密钥库中删除凭据：

`aws-vault remove {{profile}}`