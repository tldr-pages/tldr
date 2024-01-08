# vim

> Vim (Vi IMproved), un editor de texto para la línea de comandos, que proporciona varios modos para diferentes tipos de manipulación de texto.
> Pulsando `i` entra en el modo insertar. `<Esc>` regresa al modo normal, permitiendo el uso de comandos Vim.
> Más información: <https://www.vim.org>.

- Abre un archivo:

`vim {{ruta/al/archivo}}`

- Abre un archivo en un número de línea especificado:

`vim +{{número_de_línea}} {{ruta/al/archivo}}`

- Muestra el manual de Vim:

`:help<Enter>`

- Guarda y sale:

`:wq<Enter>`

- Deshaz la última operación:

`<ESC>u`

- Busca un patrón en el archivo (pulsa `n`/`N` para ir a la próxima/previa coincidencia):

`/{{patrón_a_buscar}}<Enter>`

- Realiza una sustitución de una expresión regular en el archivo completo:

`:%s/{{expresión_regular}}/{{reemplazo}}/g<Enter>`

- Muestra los números de línea:

`:set nu<Enter>`
