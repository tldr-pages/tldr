# asciinema

> Graba y reproduce sesiones de terminal, y opcionalmente compártelas en <https://asciinema.org>.
> Vea también: `terminalizer`.
> Más información: <https://docs.asciinema.org/manual/cli/usage>.

- Asocia la instalación local de `asciinema` con una cuenta de asciinema.org:

`asciinema auth`

- Haz una nueva grabación y guárdala en un archivo local (termínala con `<Ctrl d>` o teclea `exit`):

`asciinema rec {{ruta/a/grabación.cast}}`

- Reproduce una grabación de la terminal desde un archivo local:

`asciinema play {{ruta/a/grabación.cast}}`

- Reproduce una grabación de terminal alojada en <https://asciinema.org>:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Realiza una nueva grabación, limitando el tiempo de espera a un máximo de 2,5 segundos:

`asciinema rec {{[-i|--idle-time-limit]}} 2.5`

- Imprime el resultado completo de una grabación guardada localmente:

`asciinema cat {{ruta/a/grabación.cast}}`

- Carga una sesión de terminal guardada localmente en asciinema.org:

`asciinema upload {{ruta/a/grabación.cast}}`
