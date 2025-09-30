# amass enum

> Busca subdominios de un dominio.
> Más información: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Encuentra (pasivamente) subdominios de un [d]ominio:

`amass enum -d {{nombre_dominio}}`

- Encuentra subdominios de un [d]ominio y los verifica activamente intentando resolver los subdominios encontrados:

`amass enum -active -d {{nombre_dominio}} -p {{80,443,8080}}`

- Realiza una búsqueda de sub[d]ominios por fuerza bruta:

`amass enum -brute -d {{nombre_dominio}}`

- Guarda los resultados en un archivo de texto:

`amass enum -o {{archivo_de_salida}} -d {{nombre_dominio}}`

- Guarda la salida del terminal en un archivo y otros resultados detallados en un directorio:

`amass enum -o {{fichero_de_salida}} -dir {{ruta/a/directorio}} -d {{nombre_dominio}}`

- Lista todas las fuentes de datos disponibles:

`amass enum -list`
