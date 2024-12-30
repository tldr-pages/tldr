# az 登录

> 登录到 Azure。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/reference-index#az-login>。

- 交互式登录：

`az login`

- 使用客户端秘密登录服务主体：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{secret}} --tenant {{someone.onmicrosoft.com}}`

- 使用客户端证书登录服务主体：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- 使用虚拟机的系统分配身份登录：

`az login --identity`

- 使用虚拟机的用户分配身份登录：

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`