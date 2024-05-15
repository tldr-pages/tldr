# alias

> Crea alias -- palabras que son reemplazadas por una cadena de comando(s).
> Los alias son temporales en la sesión de shell actual, a no ser que estén definidos en el archivo de configuración de la shell, ej. `~/.bashrc`.
> Más información: <https://tldp.org/LDP/abs/html/aliases.html>.

- Lista todos los aliases:

`alias`

- Crea un alias genérico:

`alias {{nombre}}="{{comando}}"`

- Muestra el comando asociado a un alias:

`alias {{nombre}}`

- Elimina un alias (con el comando asociado):

`unalias {{nombre}}`

- Convierte `rm` en un comando interactivo:

`alias {{rm}}="{{rm -i}}"`

- Define `la` como un atajo para `ls -a`:

`alias {{la}}="{{ls -a}}"`
