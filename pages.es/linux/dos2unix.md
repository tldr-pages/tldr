# dos2unix

> Cambia saltos de línea con formato DOS a saltos de línea con formato Unix.
> Reemplaza CRLF con LF.
> Vea también `unix2dos`, `unix2mac`, y `mac2unix`.
> Más información: <https://manned.org/dos2unix>.

- Cambia los saltos de línea de un archivo:

`dos2unix {{ruta/al/archivo}}`

- Crea una copia con saltos de línea en formato Unix:

`dos2unix {{[-n|--newfile]}} {{ruta/al/archivo}} {{ruta/al/nuevo}}`

- Muestra información de un archivo:

`dos2unix {{[-i|--info]}} {{ruta/al/archivo}}`

- Mantiene/añade/elimina marca de orden de byte (Byte Order Mark):

`dos2unix --{{keep-bom|add-bom|remove-bom}} {{ruta/al/archivo}}`
