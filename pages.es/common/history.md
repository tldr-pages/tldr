# history

> Historial de la línea de comandos.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- Muestra el historial de comandos junto a su número de línea:

`history`

- Muestra los últimos 20 comandos (en Zsh muestra todos los comandos a partir del 20):

`history {{20}}`

- Muestra el historial con marcas de tiempo en diferentes formatos (solo disponible en Zsh):

`history -{{d|f|i|E}}`

- Limpia el historial de comandos (solo para la interfaz de comandos actual):

`history -c`

- Sobrescribe el archivo histórico con el historial de la sesión actual (comúnmente se combina con `history -c` para limpiar el historial):

`history -w`

- Borra la entrada del historial en el índice especificado:

`history -d {{índice}}`

- Añade un comando al historial sin ejecutarlo:

`history -s {{comando}}`
