# aws route53

> CLI az AWS Route53-hoz - A Route 53 egy nagy rendelkezésre állású és skálázható DNS (Domain Name System) webes szolgáltatás. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- Az összes hosztolt zóna listázása, privát és nyilvános:

`aws route53 list-hosted-zones`

- Egy zóna összes rekordjának megjelenítése:

`aws route53 list-resource-record-sets --hosted-zone-id {{zone_id}}`

- Új, nyilvános zóna létrehozása a művelet biztonságos megismétlésére szolgáló kérésazonosító használatával:

`aws route53 create-hosted-zone --name {{name}} --caller-reference {{request_identifier}}`

- Zóna törlése (ha a zóna nem alapértelmezett SOA és NS rekordokat tartalmaz, a parancs sikertelen lesz):

`aws route53 delete-hosted-zone --id {{zone_id}}`

- Egy adott zóna Amazon-kiszolgálók általi DNS-feloldásának tesztelése:

`aws route53 test-dns-answer --hosted-zone-id {{zone_id}} --record-name {{name}} --record-type {{type}}`
