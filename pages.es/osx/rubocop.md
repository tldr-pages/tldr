# rubocop

> Analiza archivos de Ruby.

- Verifica todos los archivos en el directorio actual (incluyendo subdirectorios):

`rubocop`

- Verifica uno o más archivos o directorios específicos:

`rubocop {{path/to/file}} {{path/to/directory}}`

- Guarda el output en un archivo:

`rubocop --out {{path/to/file}}`

- Muestra la lista de cops (reglas de análisis):

`rubocop --show-cops`

- Excluye una regla:

`rubocop --except {{cop_1}} {{cop_2}}`

- Ejecuta solo las reglas especificadas:

`rubocop --only {{cop_1}} {{cop_2}}`

- Autocorrige archivos (experimental):

`rubocop --auto-correct`
