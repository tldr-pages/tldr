# az account

> Az Azure előfizetési információk kezelése. A `az`, a Microsoft Azure parancssori kliensének része. További információk: <https://learn.microsoft.com/cli/azure/account>.

- A bejelentkezett fiók előfizetéseinek listájának kinyomtatása:

`az account list`

- A `subscription` beállítása az aktuálisan aktív előfizetésként:

`az account set --subscription {{subscription_id}}`

- Az aktuálisan aktív előfizetés támogatott régióinak listája:

`az account list-locations`

- Hozzáférési token nyomtatása a `MS Graph API` oldalon:

`az account get-access-token --resource-type {{ms-graph}}`

- Az aktuálisan aktív előfizetés részleteinek nyomtatása meghatározott formátumban:

`az account show --output {{json|tsv|table|yaml}}`
