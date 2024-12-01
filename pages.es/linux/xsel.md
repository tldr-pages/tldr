# xsel

> Herramienta X11 de selección y manipulación del portapapeles.
> Más información: <https://manned.org/xsel>.

- Utiliza la salida de un comando como entrada del portapapeles (clip[b]oard) (equivalente a `Ctrl + C`):

`echo 123 | xsel -ib`

- Utiliza el contenido de un archivo como entrada del portapapeles:

`cat {{ruta/al/archivo}} | xsel -ib`

- Envía el contenido del portapapeles a la terminal (equivalente a `Ctrl + V`):

`xsel -ob`

- Envía el contenido del portapapeles a un archivo:

`xsel -ob > {{ruta/al/archivo}}`

- Limpia el portapapeles:

`xsel -cb`

- Envía el contenido de la selección primaria X11 a la terminal (equivalente a clic del tercer botón del ratón):

`xsel -op`
