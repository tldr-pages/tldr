# asciinema

> Graba y reproduce sesiones de terminal, y opcionalmente compártelas en <https://asciinema.org>.
> Vea también: `terminalizer`.
> Más información: <https://docs.asciinema.org/manual/cli/usage>.

- Asocia la instalación local de `asciinema` con una cuenta de asciinema.org:

`asciinema auth`

- Realiza una nueva grabación y la guarda en un archivo local (presione `<Ctrl d>` o teclea `exit` para finalizar):

`asciinema rec {{ruta/a/grabación.cast}}`

- Reproduce una grabación de la terminal desde un archivo local:

`asciinema play {{ruta/a/grabación.cast}}`

- Reproduce una grabación de la terminal alojada en <https://asciinema.org>:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Realiza una nueva grabación, limitando el tiempo de espera a un máximo de 2,5 segundos:

`asciinema rec {{[-i|--idle-time-limit]}} 2.5`

- Imprime el resultado completo de una grabación guardada localmente:

`asciinema cat {{ruta/a/grabación.cast}}`

- Carga una sesión de terminal guardada localmente en asciinema.org:

`asciinema upload {{ruta/a/grabación.cast}}`

Transmite la sesión actual de la terminal en una página web local:

`asciinema {{[st|stream]}} --local`
