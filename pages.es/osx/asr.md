# asr

> Restaura (copia) una imagen de disco en un volumen.
> El nombre del comando significa Restauración de Software de Apple.
> Más información: <https://www.unix.com/man-page/osx/8/asr/>.

- Restaura una imagen de disco en un volumen:

`sudo asr restore --source {{nombre_de_imagen.dmg}} --target {{ruta/al/volumen}}`

- Borra el volumen deseado antes de restaurar:

`sudo asr restore --source {{nombre_de_imagen.dmg}} --target {{ruta/al/volumen}} --erase`

- Omite la verificación después de restaurar:

`sudo asr restore --source {{nombre_de_imagen.dmg}} --target {{ruta/al/volumen}} --noverify`

- Clona volúmenes sin el uso de una imagen de disco intermedia:

`sudo asr restore --source {{ruta/al/volumen}} --target {{ruta/al/volumen_clonado}}`
