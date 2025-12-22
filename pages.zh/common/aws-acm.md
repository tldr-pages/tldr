# aws acm

> AWS 证书管理器。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/acm/>.

- 导入证书：

`aws acm import-certificate --certificate-arn {{证书 ARN}} --certificate {{证书}} --private-key {{私钥}} --certificate-chain {{证书链}}`

- 列出证书：

`aws acm list-certificates`

- 描述证书：

`aws acm describe-certificate --certificate-arn {{证书 ARN}}`

- 申请证书：

`aws acm request-certificate --domain-name {{域名}} --validation-method {{验证方法}}`

- 删除证书：

`aws acm delete-certificate --certificate-arn {{证书 ARN}}`

- 列出证书验证状态：

`aws acm list-certificates --certificate-statuses {{状态}}`

- 获取证书详细信息：

`aws acm get-certificate --certificate-arn {{证书 ARN}}`

- 更新证书选项：

`aws acm update-certificate-options --certificate-arn {{证书 ARN}} --options {{选项}}`
