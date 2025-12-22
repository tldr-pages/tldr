# az login

> 登录到 Azure。
> `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- 以交互方式登录：

`az login`

- 使用客户端密码的服务主体登录：

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-服务-主体}} {{[-p|--password]}} {{密码}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- 使用客户端证书的服务主体登录：

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-服务-主体}} {{[-p|--password]}} {{路径/到/cert.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- 使用虚拟机的系统分配标识登录：

`az login {{[-i|--identity]}}`

- 使用虚拟机的用户分配标识登录：

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
