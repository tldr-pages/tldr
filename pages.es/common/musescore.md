# musescore

> MuseScore editor de música de 3 hojas.
> Vea también: `lilypond`.
> Más información: <https://musescore.org/en/handbook/4/command-line-options>.

- Utiliza un controlador de audio específico:

`musescore --audio-driver {{jack|alsa|portaudio|pulse}}`

- Establece el bitrate de salida MP3 en kbit/s:

`musescore --bitrate {{bitrate}}`

- Inicia MuseScore en modo depuración:

`musescore --debug`

- Permite características experimentales, como capas:

`musescore --experimental`

- Exporta el archivo dado al archivo de salida especificado. El tipo de archivo depende de la extensión dada:

`musescore --export-to {{archivo_de_salida}} {{archivo_de_entrada}}`

- Imprime las diferencias entre las puntuaciones (scores) dadas:

`musescore --diff {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Especifica un archivo de operaciones de importación MIDI:

`musescore --midi-operations {{ruta/al/archivo}}`
