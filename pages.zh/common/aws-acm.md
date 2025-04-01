# aws acm

> AWS 证书管理器。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/index.html>.

- 导入证书：

`aws acm import-certificate --certificate-arn {{certificate_arn}} --certificate {{certificate}} --private-key {{private_key}} --certificate-chain {{certificate_chain}}`

- 列出证书：

`aws acm list-certificates`

- 描述证书：

`aws acm describe-certificate --certificate-arn {{certificate_arn}}`

- 请求证书：

`aws acm request-certificate --domain-name {{domain_name}} --validation-method {{validation_method}}`

- 删除证书：

`aws acm delete-certificate --certificate-arn {{certificate_arn}}`

- 列出证书验证：

`aws acm list-certificates --certificate-statuses {{status}}`

- 获取证书详细信息：

`aws acm get-certificate --certificate-arn {{certificate_arn}}`

- 更新证书选项：

`aws acm update-certificate-options --certificate-arn {{certificate_arn}} --options {{options}}`
