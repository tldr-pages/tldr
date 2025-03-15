# unix2mac

> Cambia los finales de línea de estilo Unix al estilo macOS.
> Reemplaza LF con CR.
> Vea también `unix2dos`, `dos2unix` y `mac2unix`.
> Más información: <https://manned.org/unix2mac>.

- Cambia los finales de línea de un archivo:

`unix2mac {{ruta/al/archivo}}`

- Crea una copia con finales de línea de estilo macOS:

`unix2mac {{[-n|--newfile]}} {{ruta/al/archivo}} {{ruta/a/archivo_nuevo}}`

- Muestra información del archivo:

`unix2mac {{[-i|--info]}} {{ruta/al/archivo}}`

- Mantiene/añade/elimina marca de orden de byte (Byte Order Mark):

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{ruta/al/archivo}}`
