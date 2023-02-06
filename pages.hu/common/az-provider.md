# az provider

> Az erőforrás-szolgáltatók kezelése. A `azure-cli` része. További információ: <https://docs.microsoft.com/cli/azure/provider>.

- Szolgáltató regisztrálása:

`az provider register --namespace {{Microsoft.PolicyInsights}}`

- Szolgáltató leiratkozása:

`az provider unregister --namespace {{Microsoft.Automation}}`

- Az összes szolgáltató listázása egy előfizetéshez:

`az provider list`

- Információk megjelenítése egy adott szolgáltatóról:

`az provider show --namespace {{Microsoft.Storage}}`

- Egy adott szolgáltató összes erőforrástípusának felsorolása:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
