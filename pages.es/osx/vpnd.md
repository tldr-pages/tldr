# vpnd

> Escucha las conexiones VPN entrantes.
> No debería ejecutar el programa manualmente.
> Más información: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Inicia el daemon:

`vpnd`

- Ejecuta el daemon en primer plano:

`vpnd -x`

- Ejecuta el daemon en primer plano e imprime los registros en la terminal:

`vpnd -d`

- Ejecuta el daemon en primer plano, imprime los registros en la terminal y termina después de validar los argumentos:

`vpnd -n`

- Ejecuta el daemon para una configuración de servidor específica:

`vpnd -i {{identificador_de_servidor}}`

- Muestra ayuda:

`vpnd -h`
