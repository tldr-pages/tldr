# pico

> Editor de texto inspirado en Alpine Composer.
> Más información: <https://manned.org/pico>.

- Inicia el editor:

`pico {{ruta/al/archivo}}`

- Inicia el editor con el cursor situado en la línea n del archivo:

`pico +{{n}} {{ruta/al/archivo}}`

- Inicia el editor con el cursor colocado antes de la selección actual:

`pico -g {{ruta/al/archivo}}`

- Define la cadena de comillas para archivos como los de correo electrónico:

`pico -Q "{{cadena/de/comillas}}" {{ruta/al/archivo}}`

- Habilita la funcionalidad del ratón cuando se ejecuta dentro de una ventana `xterm`:

`pico -m {{ruta/al/archivo}}`

- Establece el directorio de trabajo para `pico`:

`pico -o {{ruta/al/directorio}}`

- Habilita el modo "solo lectura", que no permite realizar modificaciones:

`pico -v {{ruta/al/archivo}}`

- Muestra todos los archivos, incluidos los que comienzan con un punto:

`pico -a`
