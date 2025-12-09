# ttyplot

> Una utilidad de trazado en tiempo real para la línea de comandos con entrada de datos desde `stdin`.
> Más información: <https://github.com/tenox7/ttyplot>.

- Muestra los valores `1`, `2` y `3` (`cat` evita que ttyplot salga):

`{ echo {{1 2 3}}; cat } | ttyplot`

- Establece un título específico y unidad:

`{ echo {{1 2 3}}; cat } | ttyplot -t {{título}} -u {{unidad}}`

- Utiliza un bucle de tiempo para trazar continuamente valores aleatorios:

`{ while {{true}}; do echo {{$RANDOM}}; sleep {{1}}; done } | ttyplot`

- Analiza la salida de `ping` y la visualiza:

`ping {{8.8.8.8}} | sed -u '{{s/^.*time=//g; s/ ms//g}}' | ttyplot -t "{{ping a 8.8.8.8}}" -u {{ms}}`
