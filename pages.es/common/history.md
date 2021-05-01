# history

> Historial de la línea de comandos.
> Más información: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Muestra el historial de comandos junto a su número de línea:

`history`

- Muestra los últimos 20 comandos:

`history {{20}}`

- Limpia el historial de comandos (solo para la shell actual):

`history -c`

- Sobrescribe el archivo histórico con el historial de la shell actual (comúnmente se combina con `history -c` para limpiar el historial):

`history -w`

- Borra la entrada del historial en el índice especificado:

`history -d {{indice}}`
