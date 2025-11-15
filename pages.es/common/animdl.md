# animdl

> Recolector eficiente y veloz de datos de anime.
> Vea también: `ani-cli`.
> Más información: <https://github.com/justfoolingaround/animdl>.

- Descarga un anime específico:

`animdl download {{nombre_anime}}`

- Descarga un anime determinado, especificando un rango de episodios:

`animdl download {{nombre_anime}} {{[-r|--range]}} {{episodio_inicial}}-{{episodio_final}}`

- Descarga un anime determinado, especificando un directorio de descarga:

`animdl download {{nombre_anime}} {{[-d|--download-dir]}} {{ruta/al/directorio_de_descargas}}`

- Obtiene la URL de transmisión de un anime específico:

`animdl grab {{nombre_anime}}`

- Despliega el cronograma de los próximos animes para la siguiente semana:

`animdl schedule`

- Busca un anime específico:

`animdl search {{nombre_anime}}`

- Vea un anime específico en transmisión:

`animdl stream {{nombre_anime}}`

- Vea la transmisión del último episodio de un anime específico:

`animdl stream {{nombre_anime}} {{[-s|--special]}} latest`
