# az login

> Conectați-vă la Azure.
> O parte din `az`, clientul de linie de comandă pentru Microsoft Azure.
> Mai multe informaţii: <https://docs.microsoft.com/cli/azure/reference-index#az_login>

- Autentificare interactivă:

`az login`

- Conectați-vă cu un director de serviciu folosind un secret client:

`az login --service-principal --username {{http://azure-cli-service-principal}} --passsword {{secret}} --tenant {{someone.onmicrosoft.com}}`

- Conectați-vă cu un director de serviciu utilizând un certificat de client:

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- Autentificare folosind o identitate atribuită de sistem VM:

`az login --identity`

- Autentificare folosind identitatea atribuită unui utilizator VM:

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
