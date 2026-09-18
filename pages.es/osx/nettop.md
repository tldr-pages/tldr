# nettop

> Muestra información actualizada sobre la red.
> Más información: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- Supervisa sockets TCP y UDP de todas las interfaces:

`nettop`

- Supervisa sockets TCP de las interfaces de bucle invertido:

`nettop -m tcp -t loopback`

- Supervisa un proceso específico:

`nettop -p "{{process_id|process_name}}"`

- Muestra un resumen por proceso:

`nettop -P`

- Muestra 10 muestras de información de red:

`nettop -l 10`

- Supervisa los cambios cada 5 segundos:

`nettop -d -s 5`

- Mientras se ejecuta nettop, muestra los comandos interactivos:

`<h>`

- Muestra la ayuda:

`nettop -h`
