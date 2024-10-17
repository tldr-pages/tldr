# magick import

> Captura parte o toda la pantalla de un servidor X y guarda la imagen en un archivo.
> Vea también: `magick`.
> Más información: <https://imagemagick.org/script/import.php>.

- Captura toda la pantalla del servidor X en un archivo PostScript:

`magick import -window root {{ruta/a/salida.ps}}`

- Captura el contenido de la pantalla de un servidor X remoto en una imagen PNG:

`magick import -window root -display {{servidor_remoto}}:{{pantalla}}.{{display}} {{ruta/a/salida.png}}`

- Captura una ventana específica dada su ID mostrada por `xwininfo` en una imagen JPEG:

`magick import -window {{id_ventana}} {{ruta/a/salida.jpg}}`
