# vimdiff

> Abre dos o más archivos en Vim y muestra las diferencias entre ellos.
> Vea también `vim`.
> Más información: <https://www.vim.org>.

- Abre dos archivos y muestra las diferencias:

`vimdiff {{archivo1}} {{archivo2}}`

- Mueve el cursor a la ventana de la izquierda|derecha:

`<Ctrl> + w {{h|l}}`

- Salta a la diferencia previa:

`[c`

- Salta a la siguiente diferencia:

`]c`

- Copia la diferencia resaltada de la otra ventana a la ventana actual:

`do`

- Copia la diferencia resaltada de la ventana actual a la otra ventana:

`dp`

- Actualiza todos los resaltados y folds (plegados de texto):

`:diffupdate`

- Alterna la apertura/cierre de la fold (plegado de texto) de código resaltada:

`za`
