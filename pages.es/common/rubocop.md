# rubocop

> Analiza archivos de Ruby.
> Más información: <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Verifica todos los archivos en el directorio actual (incluyendo subdirectorios):

`rubocop`

- Verifica uno o más archivos o directorios determinados:

`rubocop {{path/to/file}} {{path/to/directory}}`

- Guarda la salida en un archivo:

`rubocop --out {{path/to/file}}`

- Muestra la lista de cops (reglas de análisis):

`rubocop --show-cops`

- Excluye una regla:

`rubocop --except {{cop_1}} {{cop_2}}`

- Ejecuta sólo determinadas reglas:

`rubocop --only {{cop_1}} {{cop_2}}`

- Autocorrige archivos (experimental):

`rubocop --auto-correct`
