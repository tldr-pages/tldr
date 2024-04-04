# vpnd

> Escucha las conexiones VPN entrantes.
> No debe invocarse manualmente.
> Más información: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Inicia el daemon:

`vpnd`

- Ejecuta el daemon en primer plano:

`vpnd -x`

- Ejecuta el daemon en primer plano e imprime los registros en el terminal:

`vpnd -d`

- Ejecuta el daemon en primer plano, imprime los registros en el terminal y luego sale tras validar los argumentos:

`vpnd -n`

- Imprime el resumen de uso y sale:

`vpnd -h`

- Ejecuta el daemon para una configuración de servidor específica:

`vpnd -i {{server_id}}`
