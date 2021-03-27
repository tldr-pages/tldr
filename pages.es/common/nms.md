# nms

> Herramienta de línea de comandos que recrea el famoso efecto de desencriptado de datos de la película Sneakers (1992).
> Más información: <https://github.com/bartobri/no-more-secrets>.

- Desencripta el texto tras presionar una tecla:

`echo "{{Hola, Mundo!}}" | nms`

- Desencripta la salida inmediatamente, sin esperar a que una tecla sea pulsada:

`{{ls -la}} | nms -a`

- Desencripta el contenido de un archivo, especificando el color de la salida:

`cat {{ruta/al/archivo}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- Limpia la pantalla antes de desencriptar:

`{{comando}} | nms -a -c`
