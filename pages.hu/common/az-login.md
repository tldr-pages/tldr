# az login

> Bejelentkezés az Azure-ba. A `az`, a Microsoft Azure parancssori kliensének része. További információ: <https://learn.microsoft.com/cli/azure/reference-index#az_login>.

- Jelentkezzen be interaktívan:

`az login`

- Jelentkezzen be egy szolgáltatási megbízóval az ügyféltitkot használva:

`az login --service-principal --username {{http://azure-cli-service-principal}} --passsword {{secret}} --tenant {{someone.onmicrosoft.com}}`

- Bejelentkezés egy szolgáltatási megbízóval ügyféltanúsítványt használva:

`az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}`

- Bejelentkezés egy VM rendszerhez rendelt azonosítójával:

`az login --identity`

- Bejelentkezés egy VM felhasználóhoz rendelt identitással:

`az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
