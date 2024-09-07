# immich-go

> Immich-Go es una herramienta abierta diseñada para subir grandes colecciones de fotos a tu servidor Immich autoalojado.
> Véase también: `immich-cli`.
> Más información: <https://github.com/simulot/immich-go>.

- Sube un archivo takeout de Google al servidor Immich:

`immich-go -server={{url_del_servidor}} -key={{clave_de_servidor}} upload {{ruta/a/archivo_takeout.zip}}`

- Importa fotos capturadas en junio del 2019, mientras se generan los álbumes automáticamente:

`immich-go -server={{url_del_servidor}} -key={{clave_del_servidor}} upload -create-albums -google-photos -date={{2019-06}} {{ruta/a/archivo_takeout.zip}}`

- Sube un archivo usando servidor y clave de un archivo de configuración:

`immich-go -use-configuration={{~/.immich-go/immich-go.json}} upload {{ruta/a/archivo_takeout.zip}}`

- Examina el contenido del servidor Immich, elimina las imágenes de menor calidad y preserva álbumes:

`immich-go -server={{url_del_servidor}} -key={{clave_del_servidor}} duplicate -yes`

- Elimina todos los álbumes creados con el patrón "YYYY-MM-DD":

`immich-go -server={{url_del_servidor}} -key={{clave_del_servidor}} tool album delete {{\d{4}-\d{2}-\d{2}}}`
