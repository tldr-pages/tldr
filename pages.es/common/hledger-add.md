# hledger add

> Registra nuevas transacciones con mensajes interactivos en la consola.
> Más información: <https://hledger.org/hledger.html#add>.

- Registra nuevas transacciones, guardándolas al archivo de diario por defecto:

`hledger add`

- Añade transacciones a `2024.journal`, pero también carga `2023.journal` para su completado:

`hledger add --file {{ruta/a/2024.journal}} --file {{ruta/a/2023.journal}}`

- Provee respuestas a las primeras 4 preguntas:

`hledger add {{today}} '{{best buy}}' {{gastos:material de oficina}} '{{$20}}'`

- Muestra la documentación y opciones de `add` usando `$PAGER`:

`hledger add --help`

- Muestra la documentación de `add` usando `info` o `man` de estar disponibles:

`hledger help add`
