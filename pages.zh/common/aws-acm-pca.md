# aws acm-pca

> AWS 证书管理器私有证书颁发机构。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html>。

- 创建私有证书颁发机构：

`aws acm-pca create-certificate-authority --certificate-authority-configuration {{ca_config}} --idempotency-token {{token}} --permanent-deletion-time-in-days {{number}}`

- 描述私有证书颁发机构：

`aws acm-pca describe-certificate-authority --certificate-authority-arn {{ca_arn}}`

- 列出私有证书颁发机构：

`aws acm-pca list-certificate-authorities`

- 更新证书颁发机构：

`aws acm-pca update-certificate-authority --certificate-authority-arn {{ca_arn}} --certificate-authority-configuration {{ca_config}} --status {{status}}`

- 删除私有证书颁发机构：

`aws acm-pca delete-certificate-authority --certificate-authority-arn {{ca_arn}}`

- 签发证书：

`aws acm-pca issue-certificate --certificate-authority-arn {{ca_arn}} --certificate-signing-request {{cert_signing_request}} --signing-algorithm {{algorithm}} --validity {{validity}}`

- 撤销证书：

`aws acm-pca revoke-certificate --certificate-authority-arn {{ca_arn}} --certificate-serial {{serial}} --reason {{reason}}`

- 获取证书详情：

`aws acm-pca get-certificate --certificate-authority-arn {{ca_arn}} --certificate-arn {{cert_arn}}`