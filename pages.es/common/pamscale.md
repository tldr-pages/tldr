# pamscale

> Escala una imagen Netpbm.
> Más información: <https://netpbm.sourceforge.net/doc/pamscale.html>.

- Escala una imagen de modo que el resultado tenga las dimensiones especificadas:

`pamscale {{[-wid|-width]}} {{ancho}} {{[-h|-height]}} {{alto}} {{ruta/a/entrada.pam}} > {{ruta/a/salida.pam}}`

- Escalar una imagen de modo que el resultado tenga la anchura especificada, manteniendo la relación de aspecto:

`pamscale {{[-wid|-width]}} {{ancho}} {{ruta/a/entrada.pam}} > {{ruta/a/salida.pam}}`

- Escalar una imagen de modo que su anchura y altura se modifiquen según los factores especificados:

`pamscale {{[-xsc|-xscale]}} {{x_factor}} {{[-ysc|-yscale]}} {{y_factor}} {{ruta/a/entrada.pam}} > {{ruta/a/salida.pam}}`

- Escalar una imagen de modo que quepa en el cuadro delimitador especificado conservando su relación de aspecto:

`pamscale -xyfit {{bbox_width}} {{bbox_height}} {{ruta/a/entrada.pam}} > {{ruta/a/salida.pam}}`

- Escalar una imagen de modo que llene completamente el cuadro especificado conservando su relación de aspecto:

`pamscale -xyfill {{ancho_cuadro}} {{box_height}} {{ruta/a/entrada.pam}} > {{ruta/a/salida.pam}}`
