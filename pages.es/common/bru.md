# bru

> CLI para Bruno, un IDE de código abierto para explorar y probar APIs.
> Más información: <https://docs.usebruno.com/cli/overview.html>.

- Ejecuta todos los archivos de petición en el directorio actual:

`bru run`

- Ejecuta una única petición en el directorio actual especificando su nombre de archivo:

`bru run {{archivo.bru}}`

- Ejecuta peticiones utilizando un entorno:

`bru run --env {{nombre_entorno}}`

- Ejecuta peticiones utilizando un entorno con una variable:

`bru run --env {{nombre_entorno}} --env-var {{nombre_variable}}={{valor_variable}}`

- Ejecuta la solicitud y guarda los resultados en un archivo de salida:

`bru run --output {{ruta/a/archivo_de_salida.json}}`

- Muestra ayuda:

`bru run --help`
