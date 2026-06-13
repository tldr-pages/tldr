# hx

> Helix, un editor de texto post-moderno, proporciona varios modos para diferentes tipos de manipulación de texto.
> Pulsando `<i>` se entra en el modo de inserción. `<Esc>` activa el modo normal, que permite el uso de los comandos de Helix.
> Más información: <https://manned.org/man/debian-forky/hx>.

- Abre un archivo:

`hx {{ruta/al/archivo}}`

- Abre archivos y los muestra uno al lado del otro:

`hx --vsplit {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Muestra el tutorial para aprender Helix (o accede a él dentro de Helix pulsando `<Esc>` y escribiendo `<:>tutor<Enter>`):

`hx --tutor`

- Cambia el tema de Helix:

`<:>theme {{nombre_tema}}`

- Guarda y se cierra:

`<:>wq<Enter>`

- Fuerza la salida sin guardar:

`<:>q!<Enter>`

- Deshace la última operación:

`<u>`

- Busca un patrón en el archivo (pulsa `<n>`/`<N>` para ir a la siguiente/anterior coincidencia):

`</>{{patrón_de_búsqueda}}<Intro>`
