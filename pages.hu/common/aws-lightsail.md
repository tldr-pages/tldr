# aws lightsail

> Az Amazon Lightsail erőforrások kezelése a CLI segítségével. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html>.

- Az összes virtuális privát szerver vagy példány listázása:

`aws lightsail get-instances`

- Az összes csomag (példányterv) listázása:

`aws lightsail list-bundles`

- Az összes elérhető példánykép vagy tervrajz listázása:

`aws lightsail list-blueprints`

- Példa létrehozása:

`aws lightsail create-instances --instance-names {{name}} --availability-zone {{region}} --bundle-id {{nano_2_0}} --blueprint-id {{blueprint_id}}`

- Egy adott példány állapotának kinyomtatása:

`aws lightsail get-instance-state --instance-name {{name}}`

- Egy adott példány leállítása:

`aws lightsail stop-instance --instance-name {{name}}`

- Egy adott példány törlése:

`aws lightsail delete-instance --instance-name {{name}}`
