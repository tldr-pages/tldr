# amass db

> Interactúa con una base de datos Amass.
> Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Lista de todas las enumeraciones realizadas en la base de datos:

`amass db -dir {{ruta/al/directorio_base_de_datos}} -list`

- Muestra resultados para un índice de enumeración y un nombre de dominio especificados:

`amass db -dir {{ruta/al/directorio_base_de_datos}} -d {{nombre_dominio}} -enum {{indice_de_lista}} -show`

- Lista todos los subdominios encontrados en un dominio dentro de una enumeración:

`amass db -dir {{ruta/al/directorio_base_de_datos}} -d {{nombre_dominio}} -enum {{indice_de_lista}} -names`

- Muestra un resumen de los subdominios encontrados dentro de una enumeración:

`amass db -dir {{ruta/al/directorio_base_de_datos}} -d {{nombre_dominio}} -enum {{indice_de_lista}} -summary`
