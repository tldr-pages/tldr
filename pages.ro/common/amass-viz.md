# amass viz

> Vizualizați informațiile colectate într-un grafic de rețea.
> Mai multe informaţii: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>

- Generarea unei vizualizări D3.js pe baza datelor bazei de date:

`amass viz -d3 -dir {{path/to/database_directory}}`

- Generați un fișier DOT bazat pe datele bazei de date:

`amass viz -dot -dir {{path/to/database_directory}}`

- Generarea unui fișier Gephi Graph Exchange XML Format (GEXF) bazat pe datele bazei de date:

`amass viz -gexf -dir {{path/to/database_directory}}`

- Generarea unui fișier Graphistry JSON pe baza datelor bazei de date:

`amass viz -graphistry -dir {{path/to/database_directory}}`

- Generarea unui fișier CSV Maltego bazat pe datele bazei de date:

`amass viz -maltego -dir {{path/to/database_directory}}`
