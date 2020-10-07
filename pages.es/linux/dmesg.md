# dmesg

> Escribe los mensajes del núcleo a la salida estándar.

- Mostrar los mensajes del núcleo:

`dmesg`

- Mostrar los mensajes de error del núcleo:

`dmesg --level err`

- Mostrar los mensajes del núcleo y seguir leyedos los nuevos, similar a `tail -f` (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -w`

- Mostrar cuanta memoria física hay disponible en este sistema:

`dmesg | grep -i memory`

- Mostrar los mensajes del núcleo, página a página:

`dmesg | less`

- Mostrar los mensajes del núcleo con una estampilla temporal (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -T`

- Mostrar los mensajes del núcleo de forma legible para humanos (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -H`

- Colorear la salida (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -L`
