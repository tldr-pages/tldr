# gcloud iam

> 配置身份和访问管理（IAM）的偏好设置和服务账户。
> 有关更多信息，参见： `gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/iam>。

- 列出资源的可授予角色：

`gcloud iam list-grantable-roles {{resource}}`

- 为组织或项目创建自定义角色：

`gcloud iam roles create {{role_name}} --{{organization|project}} {{organization|project_id}} --file {{path/to/role.yaml}}`

- 为项目创建服务账户：

`gcloud iam service-accounts create {{name}}`

- 将 IAM 策略绑定添加到服务账户：

`gcloud iam service-accounts add-iam-policy-binding {{service_account_email}} --member {{member}} --role {{role}}`

- 替换现有的 IAM 策略绑定：

`gcloud iam service-accounts set-iam-policy {{service_account_email}} {{policy_file}}`

- 列出服务账户的密钥：

`gcloud iam service-accounts keys list --iam-account {{service_account_email}}`
