# alias

> Crea alias -- palabras que son reemplazadas por una cadena de comando(s).
> Los alias son temporales en la sesión de shell actual, a no ser que estén definidos en el archivo de configuración de la shell, ej. `~/.bashrc`.
> Más información: <https://tldp.org/LDP/abs/html/aliases.html>.

- Listar todos los alias:

`alias`

- Crear un alias genérico:

`alias {{nombre}}="{{comando}}"`

- Ver el comando asociado a un alias:

`alias {{nombre}}`

- Eliminar un alias (con el comando asociado):

`unalias {{nombre}}`

- Convertir `rm` en un comando interactivo:

`alias {{rm}}="{{rm -i}}"`

- Crear `la` como un atajo para `ls -a`:

`alias {{la}}="{{ls -a}}"`
