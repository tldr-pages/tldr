# unix2dos

> Cambia los finales de línea de estilo Unix al estilo DOS.
> Reemplaza LF con CRLF.
> Vea también `unix2mac`, `dos2unix` y `mac2unix`.
> Más información: <https://manned.org/unix2dos>.

- Cambia los finales de línea de un archivo:

`unix2dos {{ruta/al/archivo}}`

- Crea una copia con finales de línea de estilo DOS:

`unix2dos {{[-n|--newfile]}} {{ruta/al/archivo}} {{ruta/a/archivo_nuevo}}`

- Muestra información del archivo:

`unix2dos {{[-i|--info]}} {{ruta/al/archivo}}`

- Mantiene/añade/elimina marca de bit de orden (Byte Order Mark):

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{ruta/al/archivo}}`
