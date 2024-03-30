# az login

> Melden Sie sich bei Azure an.
> Teil von `azure-cli` (auch bekannt als `az`).
> Weitere Informationen: <https://learn.microsoft.com/cli/azure/reference-index#az_login>.

- Melden Sie sich interaktiv an:

`az login`

- Melden Sie sich mit einem Dienstprinzipal mit dem geheimen Clientschlüssel an:

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{secret}} --tenant {{someone.onmicrosoft.com}}`

- Melden Sie sich mit einem Dienstprinzipal mithilfe des Clientzertifikats an:

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- Melden Sie sich mit der vom System zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity`

- Melden Sie sich mit der vom Benutzer zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
