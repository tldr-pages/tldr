# rubocop

> Analiza archivos de Ruby.
> Más información: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Verifica todos los archivos en el directorio actual (incluyendo subdirectorios):

`rubocop`

- Verifica uno o más archivos o directorios determinados:

`rubocop {{ruta/al/archivo_o_directorio1}} {{ruta/al/archivo_o_directorio2}}`

- Guarda la salida en un archivo:

`rubocop --out {{ruta/a/archivo}}`

- Muestra la lista de cops (reglas de análisis):

`rubocop --show-cops`

- Excluye una regla:

`rubocop --except {{cop1 cop2 ...}}`

- Ejecuta sólo determinadas reglas:

`rubocop --only {{cop1 cop2 ...}}`

- Autocorrige archivos (experimental):

`rubocop --auto-correct`
