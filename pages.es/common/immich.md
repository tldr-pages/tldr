# immich

> Immich tiene una interfaz de línea de comandos (CLI) que le permite realizar ciertas acciones desde la línea de comandos.
> Vea también: `immich-go`.
> Más información: <https://docs.immich.app/features/command-line-interface/>.

- Autentica en el servidor de Immich:

`immich login {{url_del_servidor/api}} {{clave_del_servidor}}`

- Sube unas imágenes:

`immich upload {{archivo1.jpg archivo2.jpg}}`

- Sube un directorio y sus subdirectorios:

`immich upload {{[-r|--recursive]}} {{ruta/al/directorio}}`

- Crea un álbum basado en un directorio:

`immich upload {{[-r|--recursive]}} {{ruta/al/directorio}} {{[-A|--album-name]}} "{{Vacaciones de verano}}"`

- Omite recursos que coincidan con un patrón global:

`immich upload {{[-r|--recursive]}} {{directorio/}} {{[-i|--ignore]}} {{**/Raw/** **/*.tif}}`

- Incluye archivos ocultos:

`immich upload {{[-r|--recursive]}} {{ruta/al/directorio}} {{[-H|--include-hidden]}}`
