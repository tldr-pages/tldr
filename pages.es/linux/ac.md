# ac

> Imprimir estadísticas sobre cuánto tiempo han estado conectados los usuarios.
> Más información: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Imprime cuánto tiempo ha estado conectado el usuario actual en horas:

`ac`

- Imprime cuánto tiempo han estado conectados los usuarios en horas:

`ac --individual-totals`

- Imprime cuánto tiempo ha estado conectado un usuario en particular en horas:

`ac --individual-totals {{nombre_usuario}}`

- Imprimir cuánto tiempo un usuario en particular ha estado conectado en horas por día (en total):

`ac --daily-totals --individual-totals {{nombre_usuario}}`

- Mostrar también detalles adicionales:

`ac --compatibility`
