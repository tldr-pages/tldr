# az login

> 登录 Azure。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/reference-index#az-login>。

- 交互式登录：

`az login`

- 使用客户端机密凭据的服务主体登录：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{secret}} --tenant {{someone.onmicrosoft.com}}`

- 使用客户端证书的服务主体登录：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- 使用 VM 的系统分配的身份登录：

`az login --identity`

- 使用 VM 的用户分配的身份登录：

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
