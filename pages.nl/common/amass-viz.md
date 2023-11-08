# amass viz

> Visualiseer de gevonden informatie in een netwerk grafiek.
> Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Genereer een D3.js visualisatie op basis van databasegegevens:

`amass viz -d3 -dir {{pad/naar/database_map}}`

- Genereer een DOT bestand op basis van databasegegevens:

`amass viz -dot -dir {{pad/naar/database_map}}`

- Genereer een Gephi Graph Exchange XML Format (GEXF) bestand op basis van databasegegevens:

`amass viz -gexf -dir {{pad/naar/database_map}}`

- Genereer een Graphistry JSON bestand op basis van databasegegevens:

`amass viz -graphistry -dir {{pad/naar/database_map}}`

- Genereer een Maltego CSV bestand op basis van databasegegevens:

`amass viz -maltego -dir {{pad/naar/database_map}}`
