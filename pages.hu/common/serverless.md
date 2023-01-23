# serverless

> Eszközkészlet szervermentes architektúrák telepítéséhez és üzemeltetéséhez AWS, Google Cloud, Azure és IBM OpenWhisk rendszereken. A parancsok futtatása a `serverless` paranccsal vagy annak aliasával, `sls`. További információ: <https://serverless.com/>.

- Hozzon létre egy szervermentes projektet:

`serverless create`

- Hozzon létre egy szervermentes projektet egy sablonból:

`serverless create --template {{template_name}}`

- Telepítés egy felhőszolgáltatóhoz:

`serverless deploy`

- Információk megjelenítése egy szervermentes projektről:

`serverless info`

- Egy telepített függvény meghívása:

`serverless invoke -f {{function_name}}`

- Egy projekt naplóinak követése:

`serverless logs -t`
