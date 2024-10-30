# az login

> 登入到 Azure。
> `azure-cli` 的一部分（也稱為 `az`）。
> 更多資訊：<https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- 以互動方式進行登入：

`az login`

- 使用客戶端密鑰登入服務主體：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{secret}} --tenant {{someone.onmicrosoft.com}}`

- 使用客戶端憑證登入服務主體：

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{路徑/到/憑證.pem}} --tenant {{someone.onmicrosoft.com}}`

- 使用 VM 的系統指派身份登入：

`az login --identity`

- 使用 VM 的使用者分配身份登入：

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
