# xclip

> Herramienta para manipular el portapapeles de X11, similar a `xsel`.
> Maneja la selección primaria y secundaria de X y el portapapeles (`Ctrl + C`/`Ctrl + V`).
> Más información: <https://manned.org/xclip>.

- Copia la salida de un comando a la selección primaria de X11:

`echo 123 | xclip`

- Copia la salida de un commando a una selección de X11:

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- Copia la salida de un commando al portapapeles, usando notación corta:

`echo 123 | xclip -sel clip`

- Copia el contenido de un fichero al portapapeles:

`xclip -sel clip {{archivo.txt}}`

- Copia el contenido de un fichero con formato PNG al portapapeles:

`xclip -sel clip -t image/png {{archivo.png}}`

- Copia la entrada del usuario al portapapeles:

`xclip -i`

- Imprime el contenido de la selección primaria de X11:

`xclip -o`

- Imprime el contenido del portapapeles:

`xclip -o -sel clip`
