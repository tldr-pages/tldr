# aws sts

> 安全令牌服务（Security Token Service，STS）允许为（IAM）用户或联合用户请求临时凭证。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- 获取用于访问特定 AWS 资源的临时安全凭证：

`aws sts assume-role --role-arn {{AWS 角色 ARN}}`

- 获取用于调用该操作的 IAM 用户或角色的身份信息：

`aws sts get-caller-identity`
