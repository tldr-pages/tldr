# amass db

> Interactie met een Amass database.
> Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Toon alle uitgevoerde opsommingen in de database:

`amass db -dir {{pad/naar/database_map}} -list`

- Laat de resultaten zien van een specifieke opsommingsindex en domeinnaam:

`amass db -dir {{pad/naar/database_map}} -d {{domeinnaam}} -enum {{indexlijst}} -show`

- Toon alle gevonden subdomeinen van een domeinnaam binnen de opsomming:

`amass db -dir {{pad/naar/database_map}} -d {{domeinnaam}} -enum {{indexlijst}} -names`

- Toon een samenvatting van de gevonden subdomeinen binnen de opsomming:

`amass db -dir {{pad/naar/database_map}} -d {{domeinnaam}} -enum {{indexlijst}} -summary`
