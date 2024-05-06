# immich-cli

> Immich tiene una interfaz de línea de comandos (CLI) que le permite realizar ciertas acciones desde la línea de comandos.
> Vea también: `immich-go`.
> Más información: <https://immich.app/docs/features/command-line-interface/>.

- Autentica en el servidor de Immich:

`immich login {{url_del_servidor/api}} {{clave_del_servidor}}`

- Sube unas imágenes:

`immich upload {{archivo1.jpg archivo2.jpg}}`

- Sube un directorio y sus subdirectorios:

`immich upload --recursive {{ruta/al/directorio}}`

- Crea un álbum basado en un directorio:

`immich upload --album-name "{{Vacaciones de verano}}" --recursive {{ruta/al/directorio}}`

- Omite recursos que coincidan con un patrón global:

`immich upload --ignore {{**/Raw/** **/*.tif}} --recursive {{directorio/}}`

- Incluye archivos ocultos:

`immich upload --include-hidden --recursive {{ruta/al/directorio}}`
