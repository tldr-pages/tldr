# amass enum

> Vind subdomeinen van een domein.
> Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Vind, passief, subdomeinen van een domein:

`amass enum -passive -d {{domeinnaam}}`

- Zoek subdomeinen van een domein en verifieer ze actief in een poging de gevonden subdomeinen op te lossen:

`amass enum -active -d {{domeinnaam}} -p {{80,443,8080}}`

- Doe een brute force zoekopdracht op een subdomein:

`amass enum -brute -d {{domeinnaam}}`

- Sla de resultaten op in een tekstbestand:

`amass enum -o {{uitvoer_bestand}} -d {{domeinnaam}}`

- Sla de resultaten op in een database:

`amass enum -o {{uitvoer_bestand}} -dir {{pad/naar/database_map}}`
