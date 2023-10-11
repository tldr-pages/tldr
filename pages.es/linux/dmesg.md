# dmesg

> Escribe los mensajes del núcleo a la salida estándar.
> Más información: <https://manned.org/dmesg>.

- Muestra los mensajes del núcleo:

`dmesg`

- Muestra los mensajes de error del núcleo:

`dmesg --level err`

- Muestra los mensajes del núcleo y sigue leyendo los nuevos, similar a `tail -f` (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -w`

- Muestra cuanta memoria física hay disponible en este sistema:

`dmesg | grep -i memory`

- Muestra los mensajes del núcleo, página a página:

`dmesg | less`

- Muestra los mensajes del núcleo con una estampilla temporal (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -T`

- Muestra los mensajes del núcleo de forma legible para humanos (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -H`

- Colorea la salida (disponible en los núcleos 3.5.0 y posteriores):

`dmesg -L`
