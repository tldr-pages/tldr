# ani-cli

> Un cli para navegar y ver anime.
> Más información: <https://manned.org/ani-cli>.

- Busca anime por nombre:

`ani-cli "{{nombre_del_anime}}"`

- Descarga episodio:

`ani-cli -d "{{nombre_del_anime}}"`

- Descarga una serie de episodios:

`ani-cli {{[-d|--download]}} {{[-r|--rango]}} "{{1 6}}" "{{nombre_del_anime}}"`

- Descarga la serie completa (todos los episodios):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{nombre_del_anime}}"`

- Usa VLC como reproductor multimedia:

`ani-cli -v "{{nombre_del_anime}}"`

- Especifica el episodio que desea ver:

`ani-cli -e {{numero_episodio}} "{{nombre_del_anime}}"`

- Continúa viendo el anime desde el historial:

`ani-cli -c`

- Actualiza `ani-cli`:

`ani-cli -U`
