# ftxdiff

> Compara las diferencias entre dos fuentes.
> Más información: <https://developer.apple.com/fonts>.

- Envía las diferencias a un archivo de texto específico:

`ftxdiff --output {{ruta/al/archivo_de_fontdif.txt}} {{ruta/al/archivo_ont_1.ttc}} {{ruta/al/archivo_font_2.ttc}}`

- Incluir nombres de glifos en la salida:

`ftxdiff --include-glyph-names`

- Incluir nombres unicode en la salida:

`ftxdiff --include-unicode-names`
