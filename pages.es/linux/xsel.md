# xsel

> Herramienta X11 de selección y manipulación del portapapeles.
> Más información: <https://manned.org/xsel>.

- Utiliza la salida de un comando como entrada del portapapeles (clip[b]oard) (equivalente a `<Ctrl c>`):

`echo 123 | xsel {{[-ib|--input --clipboard]}}`

- Utiliza el contenido de un archivo como entrada del portapapeles:

`cat {{ruta/al/archivo}} | xsel {{[-ib|--input --clipboard]}}`

- Envía el contenido del portapapeles a la terminal (equivalente a `<Ctrl v>`):

`xsel {{[-ob|--output --clipboard]}}`

- Envía el contenido del portapapeles a un archivo:

`xsel {{[-ob|--output --clipboard]}} > {{ruta/al/archivo}}`

- Limpia el portapapeles:

`xsel {{[-cb|--clear --clipboard]}}`

- Envía el contenido de la selección primaria X11 a la terminal (equivalente a `<MiddleClick>`):

`xsel {{[-op|--output --primary]}}`
