# az login

> Log in bij Azure.
> Onderdeel van `azure-cli` (ook bekend als `az`).
> Meer informatie: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Log interactief in:

`az login`

- Log in als een service principal met behulp van een client secret:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{secret}} {{[-t|--tenant]}} {{iemand.onmicrosoft.com}}`

- Log in als een service principal met behulp van een client certificaat:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{pad/naar/cert.pem}} {{[-t|--tenant]}} {{iemand.onmicrosoft.com}}`

- Log in met de door de systeem toegewezen identiteit van een VM:

`az login {{[-i|--identity]}}`

- Log in met de door de gebruiker toegewezen identiteit van een VM:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{abonnement_id}}/resourcegroups/{{mijn_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{mijn_id}}`
