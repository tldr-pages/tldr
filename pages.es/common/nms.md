# nms

> Herramienta de línea de comandos que recrea el famoso efecto de desencriptado de datos de la película Sneakers (1992).
> Más información: <https://github.com/bartobri/no-more-secrets>.

- Desencriptar texto tras presionar una tecla:

`echo "{{Hola, Mundo!}}" | nms`

- Desencriptar la salida inmediatamente, sin esperar a que una tecla sea pulsada:

`{{ls -la}} | nms -a`

- Desencriptar el contenido de un archivo, especificando el color del output:

`cat {{ruta/al/archivo}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- Limpiar la pantalla antes de desencriptar:

`{{comando}} | nms -a -c`
