# amass enum

> Busca subdominios de un dominio.
> Más información: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Búsqueda pasiva de subdominios de un dominio:

`amass enum -passive -d {{nombre_de_dominio}}`

- Busca subdominios de un dominio y los verifica activamente intentando resolver los subdominios encontrados:

`amass enum -active -d {{nombre_de_dominio}} -p {{80,443,8080}}`

- Hace una búsqueda en su modalidad fuerza bruta de subdominios:

`amass enum -brute -d {{nombre_de_dominio}}`

- Guarda los resultados en un archivo de texto:

`amass enum -o {{archivo_salida}} -d {{nombre_de_dominio}}`

- Guarda los resultados a una base de datos:

`amass enum -o {{archivo_salida}} -dir {{ruta/a/directorio_base_de_datos}}`
