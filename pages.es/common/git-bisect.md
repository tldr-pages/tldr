# git bisect

> Utiliza la búsqueda binaria para encontrar la confirmación que introdujo un error.
> Git salta de un lado a otro del gráfico de confirmaciones hasta alcanzar progresivamente la confirmación defectuosa.
> Más información: <https://git-scm.com/docs/git-bisect>.

- Comienza un sesión de bisecado en un rango de confirmaciones delimitada por una confirmación erróneo conocido y por uno sano conocido (normalmente más antiguo):

`git bisect start {{confirmación_errónea}} {{confirmación_buena}}`

- Por cada confirmación que `git bisect` selecciona, lo marca como "malo" o "bueno" después de probarlo:

`git bisect {{bueno|malo}}`

- Después de que `git bisect` determina con precisión la confirmación defectuosa, termina la sesión de bisecado y vuelve a la rama anterior:

`git bisect reset`

- Omite una confirmación durante una sesión de bisecado (p. ej., uno que falla las pruebas debido a un problema diferente):

`git bisect skip`
