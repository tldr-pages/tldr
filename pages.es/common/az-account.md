# az account

> Administra la información de una suscripción de Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/account>.

- Lista las suscripciones de la cuenta activa:

`az account list`

- Establece una `subscription` como la suscripción activa:

`az account set --subscription {{id_de_suscripción}}`

- Lista las regiones admitidas para la suscripción activa:

`az account list-locations`

- Imprime un token de acceso para usar con la `MS Graph API`:

`az account get-access-token --resource-type {{ms-graph}}`

- Imprime los detalles de la suscripción activa actual en un formato específico:

`az account show --output {{json|tsv|table|yaml}}`
