# nettop

> Muestra información actualizada sobre la red.
> Más información: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- Monitoriza los sockets TCP y UDP de todas las interfaces:

`nettop`

- Monitoriza sockets TCP desde interfaces Loopback:

`nettop -m {{tcp}} -t {{loopback}}`

- Supervisa un proceso específico:

`nettop -p "{{process_id|process_name}}"`

- Muestra un resumen por proceso:

`nettop -P`

- Imprime 10 muestras de información de red:

`nettop -l {{10}}`

- Monitoriza los cambios cada 5 segundos:

`nettop -d -s {{5}}`

- Mientras se ejecuta nettop, lista los comandos interactivos:

`h`

- Muestra ayuda:

`nettop -h`
