# asciinema

> Graba y reproduce sesiones de terminal, y opcionalmente compartelas en asciinema.org.
> Más información: <https://asciinema.org/>.

- Asocia el programa local de `asciinema` con una cuenta de asciinema.org:

`asciinema auth`

- Crea una nueva grabación (una vez acabada, se pregutará al usuario si la quiere cuardar en local, o subirla):

`asciinema rec`

- Crea una nueva grabación y la guarda en un archivo local:

`asciinema rec {{ruta/hacia/archivo}}.cast`

- Reproduce una grabación desde un archivo local:

`asciinema play {{ruta/hacia/archivo}}.cast`

- Reproduce una grabación desde asciinema.org:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Crea una nueva grabación, limitando el tiempo de espera máximo a 2.5 segundos:

`asciinema rec -i {{2.5}}`

- Imprime la salida completa de un archivo local de grabación:

`asciinema cat {{ruta/hacia/archivo}}.cast`

- Sube un archivo local de grabación a asciinema.org:

`asciinema upload {{ruta/hacia/archivo}}.cast`
