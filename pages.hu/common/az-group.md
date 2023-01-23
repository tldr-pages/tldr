# az group

> Erőforráscsoportok és sablonok telepítésének kezelése. A `azure-cli` webhely része. További információ: <https://docs.microsoft.com/cli/azure/group>.

- Új erőforráscsoport létrehozása:

`az group create --name {{name}} --location {{location}}`

- Ellenőrizze, hogy létezik-e erőforráscsoport:

`az group exists --name {{name}}`

- Erőforráscsoport törlése:

`az group delete --name {{name}}`

- Várjon, amíg az erőforráscsoport valamely feltétele teljesül:

`az group wait --name {{name}} --{{created|deleted|exists|updated}}`
