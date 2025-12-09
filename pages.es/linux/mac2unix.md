# mac2unix

> Cambia los finales de línea de estilo macOS al estilo Unix.
> Reemplaza CR con LF.
> Vea también `unix2dos`, `unix2mac` y `dos2unix`.
> Más información: <https://manned.org/mac2unix>.

- Cambia los finales de línea de un archivo:

`mac2unix {{ruta/al/archivo}}`

- Crea una copia con finales de línea de estilo Unix:

`mac2unix {{[-n|--newfile]}} {{ruta/al/archivo}} {{ruta/a/nuevo_archivo}}`

- Muestra información del archivo:

`mac2unix {{[-i|--info]}} {{ruta/al/archivo}}`

- Mantiene/añade/elimina marca de orden de byte (Byte Order Mark):

`mac2unix --{{keep-bom|add-bom|remove-bom}} {{ruta/al/archivo}}`
