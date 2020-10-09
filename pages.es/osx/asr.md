# asr

> Restaura (copia) una imagen de disco en un volumen.
> El nombre del comando significa Restauración de Software de Apple.

- Restaura una imagen de disco en un volumen:

`sudo asr restore --source {{nombre_de_imagen}}.dmg --target {{ruta/al/volumen}}`

- Borrar el volumen deseado antes de restaurar:

`sudo asr restore --source {{image_name}}.dmg --target {{path/to/volume}} --erase`

- Omitir verificación después de restaurar:

`sudo asr restore --source {{image_name}}.dmg --target {{path/to/volume}} --noverify`

- Clonar volúmenes sin el uso de una imagen de disco intermedia

`sudo asr restore --source {{path/to/volume}} --target {{path/to/cloned_volume}}`
