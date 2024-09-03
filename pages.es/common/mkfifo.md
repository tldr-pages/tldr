# mkfifo

> Crea FIFOs (llamadas pipes).
> Más información: <https://www.gnu.org/software/coreutils/mkfifo>.

- Crea un pipe con nombre en una ruta dada:

`mkfifo {{ruta/a/pipe}}`

- Envía datos a través de un pipe con nombre y envía el comando al fondo:

`echo {{"Hola Mundo"}} > {{ruta/a/pipe}} &`

- Recibe datos a través de un pipe con nombre:

`cat {{ruta/a/pipe}}`
