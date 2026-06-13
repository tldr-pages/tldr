# nvim

> Neovim, un editor de texto para programadores basado en Vim, ofrece varios modos para diferentes tipos de manipulación de texto.
> Al pulsar `<i>` en modo normal se entra en modo de inserción. `<Esc>` o `<Ctrl c>` vuelve al modo normal, lo cual no permite la inserción de texto normal.
> Vea también: `vim`, `vimtutor`, `vimdiff`.
> Más información: <https://neovim.io/>.

- Abre un archivo:

`nvim {{ruta/al/archivo}}`

- Entra en el modo de edición de texto (modo de inserción):

`<Esc><i>`

- Copia ("yank") o corta ("delete") la línea actual (pégala con `<p>`):

`<Esc>{{<y><y>|<d><d>}}`

- Entra en modo normal y deshace la última operación:

`<Esc><u>`

- Busca un patrón en el archivo (pulsa `<n>`/`<N>` para ir a la coincidencia siguiente/anterior):

`<Esc></>{{patrón_búsqueda}}<Enter>`

- Realiza una sustitución `regex` en todo el archivo:

`<Esc><:>%s/{{expresión_regular}}/{{texto_reemplazo}}/g<Enter>`

- Entra en modo normal y guarda (escribe) el archivo, y sale:

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- Sale sin guardar:

`<Esc><:>q!<Enter>`
