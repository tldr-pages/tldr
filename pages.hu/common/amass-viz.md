# amass viz

> Az összegyűjtött információk hálózati gráfban való megjelenítése. További információ: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- D3.js vizualizáció generálása adatbázis-adatok alapján:

`amass viz -d3 -dir {{path/to/database_directory}}`

- DOT fájl generálása adatbázisadatok alapján:

`amass viz -dot -dir {{path/to/database_directory}}`

- Gephi Graph Exchange XML Format (GEXF) fájl generálása adatbázis-adatok alapján:

`amass viz -gexf -dir {{path/to/database_directory}}`

- Graphistry JSON fájl generálása adatbázis-adatok alapján:

`amass viz -graphistry -dir {{path/to/database_directory}}`

- Maltego CSV fájl generálása adatbázis-adatok alapján:

`amass viz -maltego -dir {{path/to/database_directory}}`
