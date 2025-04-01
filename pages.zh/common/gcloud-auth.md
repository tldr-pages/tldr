# gcloud auth

> 授予和撤销 `gcloud` 的授权，并管理凭证。
> 参见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/auth>。

- 使用 Google Cloud 用户凭证授权 `gcloud` CLI 访问 Google Cloud，并将当前账户设置为活动状态：

`gcloud auth login`

- 使用服务账户凭证授权 Google Cloud 访问，类似于 `gcloud auth login`：

`gcloud auth activate-service-account`

- 管理 Cloud 客户端库的默认应用凭证 (ADC)：

`gcloud auth application-default`

- 显示当前系统上已认证的 Google Cloud 账户列表：

`gcloud auth list`

- 显示当前账户的访问令牌：

`gcloud auth print-access-token`

- 移除某个账户的访问凭证：

`gcloud auth revoke`