# gcloud 身份验证

> 授予和撤销对 `gcloud` 的授权，并管理凭据。
> 另见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/auth>。

- 使用 Google Cloud 用户凭据授权 Google Cloud 访问 `gcloud` CLI，并将当前帐户设置为活动帐户：

`gcloud auth login`

- 使用服务帐户凭据授权 Google Cloud 访问，类似于 `gcloud auth login`：

`gcloud auth activate-service-account`

- 管理 Cloud Client Libraries 的应用程序默认凭据 (ADC)：

`gcloud auth application-default`

- 显示当前在系统上经过身份验证的 Google Cloud 帐户列表：

`gcloud auth list`

- 显示当前帐户的访问令牌：

`gcloud auth print-access-token`

- 移除帐户的访问凭据：

`gcloud auth revoke`