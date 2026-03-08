# lilypond

> Compila música y/o produce MIDI a partir de un archivo.
> Vea también: `musescore`.
> Más información: <https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage>.

- Compila un archivo lilypond en un PDF:

`lilypond {{ruta/al/archivo}}`

- Compila en el formato especificado:

`lilypond {{[-f|--format]}} {{formato_dump}} {ruta/al/archivo}}`

- Compila el archivo especificado, suprimiendo las actualizaciones de progreso:

`lilypond {{[-s|--silent]}} {ruta/al/archivo}}`

- Compila el archivo especificado y especificar también el nombre del archivo de salida:

`lilypond {{[-o|--output]}} {{ruta/al/archivo_de_salida}} {{ruta/al/archivo_de_entrada}}`

- Muestra la versión:¢

`lilypond {{[-v|--version]}}`
