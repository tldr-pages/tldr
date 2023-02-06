# sfdx

> Parancssoros eszköz a Salesforce-szervezettel való fejlesztés és építés automatizálásához. További információ: <https://developer.salesforce.com/tools/sfdxcli>.

- Egy Salesforce szervezet engedélyezése:

`sfdx force:auth:web:login --setalias {{organization}} --instanceurl {{organization_url}}`

- Az összes engedélyezett szervezet felsorolása:

`sfdx force:org:list`

- Egy adott szervezet megnyitása az alapértelmezett webböngészőben:

`sfdx force:org:open --targetusername {{organization}}`

- Egy adott szervezetre vonatkozó információk megjelenítése:

`sfdx force:org:display --targetusername {{organization}}`

- Forrás metaadatok átvitele egy szervezethez:

`sfdx force:source:push --targetusername {{organization}}`

- Forrás metaadatok lehívása egy szervezetből:

`sfdx force:source:pull --targetusername {{organization}}`

- Jelszó generálása a szervezet bejelentkezett felhasználójának:

`sfdx force:user:password:generate --targetusername {{organization}}`

- Engedélykészlet hozzárendelése a szervezet bejelentkezett felhasználójához:

`sfdx force:user:permset:assign --permsetname {{permission_set_name}} --targetusername {{organization}}`
