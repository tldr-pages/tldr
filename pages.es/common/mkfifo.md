# mkfifo

> Crea FIFOs (named pipes) (pipes nombrados).
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Crea un pipe nombrado en una ruta específica:

`mkfifo {{ruta/al/pipe}}`

- Envía datos a través de un pipe nombrado ejecutando el comando en segundo plano:

`echo "{{Hola Mundo}}" > {{ruta/al/pipe}} &`

- Recibe datos a través de un pipe nombrado:

`cat {{ruta/al/pipe}}`

- Comparte tu sesión de la terminal en tiempo real:

`mkfifo {{ruta/al/pipe}}; script -f {{ruta/al/pipe}}`
