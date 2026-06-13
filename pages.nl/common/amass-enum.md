# amass enum

> Vind subdomeinen van een domein.
> Meer informatie: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Vind, passief, subdomeinen van een [d]omein:

`amass enum -d {{domeinnaam}}`

- Zoek subdomeinen van een [d]omein en verifieer ze actief in een poging de gevonden subdomeinen op te lossen:

`amass enum -active -d {{domeinnaam}} -p {{80,443,8080}}`

- Doe een brute force zoekopdracht op een sub[d]omein:

`amass enum -brute -d {{domeinnaam}}`

- Sla de resultaten op in een tekstbestand:

`amass enum -o {{uitvoer_bestand}} -d {{domeinnaam}}`

- Sla de resultaten op in een database en andere gedetailleerde output naar een map:

`amass enum -o {{uitvoer_bestand}} -dir {{pad/naar/database_map}} -d {{domeinnaam}}`

- Toon alle beschikbare databronnen:

`amass enum -list`
