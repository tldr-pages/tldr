# amass viz

> Visualize gathered information in a network graph.
> Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Genera una visualización D3.js basada en los datos de la base de datos:

`amass viz -d3 -dir {{ruta/a/directorio_de_base_de_datos}}`

- Genera un archivo DOT a partir de los datos de la base de datos:

`amass viz -dot -dir {{ruta/a/directorio_de_base_de_datos}}`

- Genera de un archivo en formato Gephi Graph Exchange XML (GEXF) a partir de los datos de la base de datos:

`amass viz -gexf -dir {{ruta/a/directorio_de_base_de_datos}}`

- Genera un archivo Graphistry JSON a partir de los datos de la base de datos:

`amass viz -graphistry -dir {{ruta/a/directorio_de_base_de_datos}}`

- Genera un archivo CSV Maltego a partir de los datos de la base de datos:

`amass viz -maltego -dir {{ruta/a/directorio_de_base_de_datos}}`
