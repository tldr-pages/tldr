# aws sts

> 安全令牌服务 (STS) 允许请求 IAM 用户或联合用户的临时凭证。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- 获取临时安全凭证以访问特定的 AWS 资源：

`aws sts assume-role --role-arn {{aws_role_arn}}`

- 获取用于调用操作的凭证所属的 IAM 用户或角色：

`aws sts get-caller-identity`
