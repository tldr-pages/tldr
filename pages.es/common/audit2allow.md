# audit2allow

> Analiza los registros en busca de mensajes relativos a permisos denegados.
> Genera un informe de las reglas de Type Enforcement (TE) que podrían permitir operaciones con éxito.
> Vea también: `audit2why`.
> Más información: <https://manned.org/audit2allow>.

- Muestra todos los mensajes generados en los registros de auditoría y mensajes:

`audit2allow {{[-a|--all]}}`

- Mostrar todos los mensajes generados desde el último arranque:

`audit2allow {{[-b|--boot]}}`

- Muestra información detallada sobre los mensajes generados:

`audit2allow {{[-e|--explain]}}`

- Activa el modo de salida detallada:

`audit2allow {{[-v|--verbose]}}`

- Utiliza macros instaladas para generar una política de referencia:

`audit2allow {{[-R|--reference]}}`

- Especifica un archivo de política para su posterior análisis:

`audit2allow {{[-p|--policy]}} {{ruta/a/archivo_de_directiva}}`

- Limita el análisis a los mensajes con un tipo especificado en `regex`:

`audit2allow {{[-t|--type]}} {{tipo_regex}}`

- Muestra la ayuda:

`audit2allow {{[-h|--help]}}`
