# az appconfig

> Alkalmazáskonfigurációk kezelése az Azure-on. A `az`, a Microsoft Azure parancssori kliensének része. További információ: <https://learn.microsoft.com/cli/azure/appconfig>.

- Alkalmazáskonfiguráció létrehozása:

`az appconfig create --name {{name}} --resource-group {{group_name}} --location {{location}}`

- Egy adott App konfiguráció törlése:

`az appconfig delete --resource-group {{rg_name}} --name {{appconfig_name}}`

- Az aktuális előfizetés alá tartozó összes App konfiguráció listázása:

`az appconfig list`

- Az összes App konfiguráció listázása egy adott erőforráscsoport alatt:

`az appconfig list --resource-group {{rg_name}}`

- Egy alkalmazáskonfiguráció tulajdonságainak megjelenítése:

`az appconfig show --name {{appconfig_name}}`

- Egy adott alkalmazáskonfiguráció frissítése:

`az appconfig update --resource-group {{rg_name}} --name {{appconfig_name}}`
