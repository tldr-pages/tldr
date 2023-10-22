# amass track

> Seguimiento de las diferencias entre enumeraciones del mismo dominio.
> Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Muestra la diferencia entre las últimas enumeraciones de un dominio específico:

`amass track -dir {{ruta/a/directorio_de_base_de_datos}} -d {{nombre_dominio}} -last {{1..infinity}}`

- Muestra la diferencia entre un momento determinado y la última enumeración:

`amass track -dir {{ruta/a/directorio_de_base_de_datos}} -d {{nombre_dominio}} -since {{01/02 15:04:05 2006 MST}}`
