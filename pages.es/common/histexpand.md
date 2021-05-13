# history expansion

> Reutiliza y expande el historial de la shell en `sh`, `bash`, `zsh`, `rbash` y `ksh`.
> Más información: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Ejecuta el último comando:

`!!`

- Ejecuta el último comando como administrador:

`sudo !!`

- Ejecuta un comando con el último argumento del último comando:

`{{comando}} !$`

- Ejecuta un comando con el primer argumento del comando anterior:

`{{comando}} !^`

- Ejecuta el comando `n` líneas atrás en el historial:

`!-{{n}}`

- Ejecuta el último comando con el prefijo `cadena`:

`!{{cadena}}`

- Ejecuta el último comando, reemplazando `cadena1` por `cadena2`:

`^{{cadena1}}^{{cadena2}}^`

- Realiza una expansión del historial, pero muestra el comando que se ejecutaría en lugar de ejecutarlo realmente:

`{{!-n}}:p`
