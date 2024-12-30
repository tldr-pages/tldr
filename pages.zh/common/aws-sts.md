# aws sts

> 安全令牌服务 (STS) 允许请求临时凭证，以供 (IAM) 用户或联合用户使用。
> 更多信息请参见：<https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- 获取访问特定 AWS 资源的临时安全凭证：

`aws sts assume-role --role-arn {{aws_role_arn}}`

- 获取用于调用操作的 IAM 用户或角色的凭证：

`aws sts get-caller-identity`