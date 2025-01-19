# tac

> Muestra y concatena archivos con las líneas en orden inverso.
> Vea también: `cat`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Concatena archivos específicos en orden inverso:

`tac {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Muestra `stdin` en orden inverso:

`{{cat ruta/al/archivo}} | tac`

- Usa un separador específico:

`tac --separator {{,}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Usa una expresión regular específica como separador:

`tac --regex --separator {{[,;]}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Usa un separador antes de cada archivo:

`tac --before {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
