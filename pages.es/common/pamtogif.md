# pamtogif

> Convierte una imagen Netpbm en una imagen GIF no animada.
> Vea también: `giftopnm`, `gifsicle`.
> Más información: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Convierte una imagen Netpbm en una imagen GIF no animada:

`pamtogif {{ruta/a/imagen.pam}} > {{ruta/a/imagen_de_salida.gif}}`

- Marca el color especificado como transparente en el archivo GIF de salida:

`pamtogif -transparent {{color}} {{ruta/a/imagen.pam}} > {{ruta/a/imagen_de_salida.gif}}`

- Incluye el texto especificado como comentario en el archivo GIF de salida:

`pamtogif -comment "{{¡Hola Mundo!}}" {{ruta/a/imagen.pam}} > {{ruta/a/imagen_de_salida.gif}}`
