# nano

> Editor sencillo y fácil de usar. Un clon libre y mejorado de `Pico`.
> Vea también: `emacs`, `helix`, `vim`.
> Más información: <https://nano-editor.org/dist/latest/nano.html>.

- Inicia el editor:

`nano`

- Inicia el editor sin usar archivos de configuración:

`nano {{[-I|--ignorercfiles]}}`

- Abre archivos específicos, moviéndose al siguiente archivo cuando se cierra el anterior:

`nano {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Abre un archivo específico, posicionando el cursor en la línea y columna específica:

`nano +{{línea}},{{columna}} {{ruta/al/archivo}}`

- Abre un archivo específico y activa el ajuste de línea suave (wrapping):

`nano {{[-S|--softwrap]}} {{ruta/al/archivo}}`

- Abre un archivo específico y sangra nuevas líneas al nivel de las líneas anteriores:

`nano {{[-i|--autoindent]}} {{ruta/al/archivo}}`

- Abre nano y crea un archivo de respaldo (`ruta/al/archivo~`) cuando se guardan las ediciones:

`nano {{[-B|--backup]}} {{ruta/al/archivo}}`
