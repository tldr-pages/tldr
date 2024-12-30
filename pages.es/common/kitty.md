# kitty

> Un emulador rápido de una terminal basado en GPU rico en características.
> Más información: <https://sw.kovidgoyal.net/kitty/>.

- Abre una nueva terminal:

`kitty`

- Abre una terminal con el título especificado para la ventana:

`kitty --title "{{título}}"`

- Inicia el selector de temas incorporado:

`kitty +kitten themes`

- Muestra una imagen en la terminal:

`kitty +kitten icat {{ruta/a/la/imagen}}`

- Copia el contenido de `stdin` al portapapeles:

`echo {{ejemplo}} | kitty +kitten clipboard`
