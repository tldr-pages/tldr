# az login

> Log in to Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Log in interactively:

`az login`

- Log in with a service principal using a client secret:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{secret}} --tenant {{someone.onmicrosoft.com}}`

- Log in with a service principal using a client certificate:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{path/to/cert.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Log in using a VM's system assigned identity:

`az login {{[-i|--identity]}}`

- Log in using a VM's user assigned identity:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
