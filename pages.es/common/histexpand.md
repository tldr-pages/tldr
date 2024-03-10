# history expansion

> Reutiliza y expande el historial del shell en `sh`, Bash, Zsh, `rbash` y `ksh`.
> Más información: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Ejecuta el comando anterior como root (`!!` se sustituye por el comando anterior):

`sudo !!`

- Ejecuta un comando con el último argumento del comando anterior:

`{{comando}} !$`

- Ejecuta un comando con el primer argumento del comando anterior:

`{{comando}} !^`

- Ejecuta el `n` comando del historial:

`!{{n}}`

- Ejecuta el comando `n` líneas atrás en el historial:

`!-{{n}}`

- Ejecuta el comando más reciente que contenga `cadena`:

`!?{{cadena}}?`

- Ejecuta el comando anterior, sustituyendo "cadena1" por "cadena2":

`^{{cadena1}}^{{cadena2}}^`

- Realiza una expansión del historial, pero imprimiendo el comando que se ejecutaría en lugar de ejecutarlo realmente:

`{{!-n}}:p`
