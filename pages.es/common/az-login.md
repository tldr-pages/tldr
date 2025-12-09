# az login

> Inicia sesión en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Inicia sesión de manera interactiva:

`az login`

- Inicia sesión con una entidad de servicio mediante un secreto de cliente:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{secreto}} --tenant {{someone.onmicrosoft.com}}`

- Inicia sesión con una entidad de servicio mediante un certificado de cliente:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{ruta/al/certificado.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Inicia sesión con una identidad administrada al sistema de una máquina virtual:

`az login {{[-i|--identity]}}`

- Inicia sesión mediante la identidad administrada al usuario de una máquina virtual:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{identificador_de_subscripción}}/resourcegroups/{{mi_grupo_de_recursos}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{mi_identificador}}`
