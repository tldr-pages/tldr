# theHarvester

> Una herramienta diseñada para las primeras etapas en una prueba de penetración.
> Más información: <https://github.com/laramies/theHarvester>.

- Recopila información sobre un dominio utilizando Google:

`theHarvester --domain {{nombre_de_dominio}} --source google`

- Recopila información sobre un dominio utilizando varias fuentes:

`theHarvester --domain {{nombre_de_dominio}} --source {{duckduckgo,bing,crtsh}}`

- Cambia el límite de resultados con los que trabajar:

`theHarvester --domain {{nombre_de_dominio}} --source {{google}} --limit {{200}}`

- Guarda el resultado en dos archivos en formato XML y HTML:

`theHarvester --domain {{nombre_de_dominio}} --source {{google}} --file {{nombre_de_archivo_de_salida}}`

- Muestra ayuda:

`theHarvester --help`
