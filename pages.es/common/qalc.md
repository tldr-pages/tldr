# qalc

> Calculadora de línea de comandos potente y fácil de usar.
> Vea también: `bc`.
> Más información: <https://qalculate.github.io/manual/qalc.html>.

- Lanzamiento en modo [i]nteractivo:

`qalc {{--interactive}}`

- Ejecuta en modo [t]erse (solo imprime los resultados):

`qalc --terse`

- Actualiza los tipos de cambio:

`qalc --exrates`

- Realiza cálculos de forma no interactiva:

`qalc {{66+99|2^4|6 pies a cm|1 bitcoin a USD|20 kmph a mph|...}}`

- Lista todas las funciones/prefijos/unidades/variables soportadas:

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- Ejecuta comandos desde un archivo:

`qalc --file {{ruta/a/archivo}}`
