# paste

> Combina líneas de archivos.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- Une todas las líneas en una sola línea, utilizando `TAB` como delimitador:

`paste {{[-s|--serial]}} {{ruta/al/archivo}}`

- Une todas las líneas en una sola línea, utilizando el delimitador especificado:

`paste {{[-s|--serial]}} {{[-d|--delimiters]}} {{delimitador}} {{ruta/al/archivo}}`

- Combina dos archivos uno al lado del otro, cada uno en su columna, utilizando `TAB` como delimitador:

`paste {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Combina dos archivos uno al lado del otro, cada uno en su columna, utilizando el delimitador especificado:

`paste {{[-d|--delimiters]}} {{delimitador}} {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Combina dos archivos, con líneas añadidas alternativamente:

`paste {{[-d|--delimiters]}} '\n' {{ruta/al/archivo1}} {{ruta/al/archivo2}}`
