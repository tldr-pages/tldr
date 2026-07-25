# vpnd

> Escucha las conexiones VPN entrantes.
> No debería ejecutar el programa manualmente.
> Más información: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Inicia el programa residente:

`vpnd`

- Ejecuta el programa residente en primer plano:

`vpnd -x`

- Ejecuta el programa residente en primer plano e imprime los registros en la terminal:

`vpnd -d`

- Ejecuta el programa residente en primer plano, imprime los registros en la terminal y termina después de validar los argumentos:

`vpnd -n`

- Ejecuta el programa residente para una configuración de servidor específica:

`vpnd -i {{identificador_de_servidor}}`

- Muestra la ayuda:

`vpnd -h`
