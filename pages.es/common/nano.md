# nano

> Editor sencillo y fácil de usar. Un clon libre y mejorado de Pico.
> Más información: <https://nano-editor.org>.

- Abre un nuevo archivo en nano:

`nano`

- Abre un archivo específico:

`nano {{ruta/al/archivo}}`

- Abre un archivo específico, posicionando el cursor en la línea y columna específica:

`nano +{{linea}},{{columna}} {{ruta/al/archivo}}`

- Abre un archivo específico y activa el ajuste de línea:

`nano --softwrap {{ruta/al/archivo}}`

- Abre un archivo específico y sangra nuevas líneas a la sangría de las líneas anteriores:

`nano --autoindent {{ruta/al/archivo}}`

- Abre nano y create un archivo de resguardo (`archivo~`)  cuando se guardan las ediciones:

`nano --backup {{ruta/al/archivo}}`
