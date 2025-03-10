# helix

> Helix, un editor de texto postmoderno, ofrece varios modos para diferentes tipos de manipulación de texto.
> Al presionar `<i>` entra en modo de inserción. `<Esc>` entra en modo normal, lo que permite el uso de comandos Helix.
> Más información: <https://helix-editor.com>.

- Abre un archivo:

`helix {{ruta/al/archivo}}`

- Abre archivos y los muestra uno al lado del otro:

`helix --vsplit {{ruta/al/archivo1 ruta/al/archivo2}}`

- Muestra el tutorial para aprender Helix (o acceder al mismo dentro de Helix presionando `<Esc>` y escribiendo `<:>tutor<Enter>`):

`helix --tutor`

- Cambia el tema (theme) de Helix:

`<:>theme {{nombre_tema}}<Enter>`

- Guarda y sale:

`<:>wq<Enter>`

- Sale a la fuerza sin guardar:

`<:>q!<Enter>`

- Deshace la última operación:

`<u>`

- Busca un patrón en el archivo (al presionar `<n>`/`<N>` va a la coincidencia siguiente/anterior):

`</>{{patrón_de_búsqueda}}<Enter>`
