# aws acm-pca

> AWS Certificate Manager 私有证书颁发机构。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/acm-pca/>.

- 创建一个私有证书颁发机构：

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{证书颁发机构配置}} --idempotency-token {{幂等性令牌}} --permanent-deletion-time-in-days {{天数}}`

- 描述一个私有证书颁发机构：

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{证书颁发机构 ARN}}`

- 列出私有证书颁发机构：

`aws acm-pca list-certificate-authorities`

- 更新一个证书颁发机构：

`aws acm-pca update-certificate-authority --certificate-authority-arn {{证书颁发机构 ARN}} --certificate-authority-configuration {{证书颁发机构配置}} --status {{状态}}`

- 删除一个私有证书颁发机构：

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{证书颁发机构 ARN}}`

- 颁发一个证书：

`aws acm-pca issue-certificate --certificate-authority-arn {{证书颁发机构 ARN}} --certificate-signing-request {{证书签名请求}} --signing-algorithm {{算法}} --validity {{有效期}}`

- 吊销一个证书：

`aws acm-pca revoke-certificate --certificate-authority-arn {{证书颁发机构 ARN}} --certificate-serial {{证书序列号}} --reason {{原因}}`

- 获取证书详细信息：

`aws acm-pca get-certificate --certificate-authority-arn {{证书颁发机构 ARN}} --certificate-arn {{证书 ARN}}`
