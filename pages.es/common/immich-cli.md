# immich-cli

> Immich tiene una interfaz de línea de comandos (CLI) que le permite realizar ciertas acciones desde la línea de comandos.
> Vea también: `immich-go`.
> Más información: <https://immich.app/docs/features/command-line-interface/>.

- Autenticarse en el servidor de Immich:

`immich login {{http://192.168.1.69:2283/api}} {{HFEJ38DNSDUEG}}`

- Sube algunas imágenes:

`immich upload {{archivo1.jpg archivo2.jpg}}`

- Sube un directorio incluyendo subdirectorios:

`immich upload --recursive {{directorio/}}`

- Crea un álbum basado en un directorio:

`immich upload --album-name {{"Vacaciones de verano"}} --recursive {{directorio/}}`

- Omite recursos que coincidan con un patrón global:

`immich upload --ignore {{**/Raw/** **/*.tif}} --recursive {{directorio/}}`

- Incluye archivos ocultos:

`immich upload --include-hidden --recursive {{directorio/}}`
