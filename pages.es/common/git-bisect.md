# git bisect

> Utiliza la búsqueda binaria para encontrar la confirmación que introdujo un error.
> Git salta de un lado a otro del gráfico de confirmaciones hasta alcanzar progresivamente la confirmación defectuosa.
> Más información: <https://git-scm.com/docs/git-bisect>.

- Comienza una sesión de bisecado en un rango de confirmaciones delimitado por una confirmación errónea conocida y por una sana conocida (normalmente más antigua):

`git bisect start {{confirmación_errónea}} {{confirmación_buena}}`

- Para cada confirmación que `git bisect` seleccione, marcala como "mala" (`bad`) o "buena" (`good`) después de probarla para el problema:

`git bisect {{good|bad}}`

- Termina la sesión de bisecado y vuelve a la rama anterior después de que `git-bisect` determine con precisión la confirmación defectuosa:

`git bisect reset`

- Omite una confirmación durante una sesión de bisecado (p. ej. una que falla las pruebas debido a un problema diferente):

`git bisect skip`

- Muestra un registro de lo que se ha hecho hasta el momento:

`git bisect log`
