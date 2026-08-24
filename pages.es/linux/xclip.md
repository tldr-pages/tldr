# xclip

> Herramienta para manipular el portapapeles de X11, similar a `xsel`.
> Maneja la selección primaria y secundaria de X y el portapapeles (`<Ctrl c>`/`<Ctrl v>`).
> Vea también: `wl-copy`.
> Más información: <https://manned.org/xclip>.

- Copia la salida de un comando a la selección primaria de X11:

`echo 123 | xclip`

- Copia la salida de un commando a una selección de X11:

`echo 123 | xclip {{[-se|-selection]}} {{primary|secondary|clipboard}}`

- Copia la salida de un commando al portapapeles, usando notación corta:

`echo 123 | xclip {{[-se|-selection]}} {{[c|clipboard]}}`

- Copia el contenido de un fichero al portapapeles:

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{archivo.txt}}`

- Copia el contenido de un fichero con formato PNG al portapapeles:

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png {{archivo.png}}`

- Copia la entrada del usuario al portapapeles:

`xclip {{[-i|-in]}}`

- Imprime el contenido de la selección primaria de X11:

`xclip {{[-o|-out]}}`

- Imprime el contenido del portapapeles:

`xclip {{[-o|-out]}} {{[-se|-selection]}} {{[c|clipboard]}}`
