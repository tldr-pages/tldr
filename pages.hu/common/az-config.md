# az config

> Az Azure CLI konfiguráció kezelése. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/config>.

- Az összes konfiguráció kinyomtatása:

`az config get`

- Egy adott szakasz konfigurációinak nyomtatása:

`az config get {{section_name}}`

- Konfiguráció beállítása:

`az config set {{configuration_name}}={{value}}`

- Konfiguráció beállításának visszavonása:

`az config unset {{configuration_name}}`
