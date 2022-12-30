# az login

> Log in to Azure.
> Part of `az`, the command-line client for Microsoft Azure.
> More information: <https://learn.microsoft.com/cli/azure/reference-index#az_login>.

- Log in interactively:

`az login`

- Log in with a service principal using a client secret:

`az login --service-principal --username {{http://azure-cli-service-principal}} --passsword {{secret}} --tenant {{someone.onmicrosoft.com}}`

- Log in with a service principal using a client certificate:

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- Log in using a VM's system assigned identity:

`az login --identity`

- Log in using a VM's user assigned identity:

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
