# amass viz

> Visualize gathered information in a network graph.
> Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Genere una visualización D3.js basada en datos específicos de la base de datos::

`amass viz -d3 -dir {{ruta/al/directorio_de_base_de_datos}}`

- Genera un archivo DOT a partir de los datos específicos de la base de datos:

`amass viz -dot -dir {{ruta/al/directorio_de_base_de_datos}}`

- Genera un archivo en formato Gephi Graph Exchange XML (GEXF) a partir específicos de los datos de la base de datos:

`amass viz -gexf -dir {{ruta/al/directorio_de_base_de_datos}}`

- Genera un archivo Graphistry JSON a partir de los datos específicos de la base de datos:

`amass viz -graphistry -dir {{ruta/al/directorio_de_base_de_datos}}`

- Genera un archivo CSV Maltego a partir de los datos específicos de la base de datos:

`amass viz -maltego -dir {{ruta/al/directorio_de_base_de_datos}}`
