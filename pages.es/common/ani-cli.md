# ani-cli

> Una interface de línea de comando para navegar y ver anime.
> Más información: <https://manned.org/ani-cli>.

- Busca anime por nombre:

`ani-cli "{{nombre_del_anime}}"`

- Descarga un episodio:

`ani-cli {{[-d|--download]}} "{{nombre_del_anime}}"`

- Descarga una serie de episodios:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{nombre_del_anime}}"`

- Descarga toda la serie (un rango de todos los episodios):

`ani-cli {{[-d|--download]}} {{[-r|--rango]}} "1 -1" "{{nombre_del_anime}}"`

- Usa VLC como reproductor multimedia:

`ani-cli {{[-v|-vlc]}} "{{nombre_del_anime}}"`

- Ve un episodio concreto:

`ani-cli {{[-e|--episode]}} {{número_episodio}} "{{nombre_del_anime}}"`

- Continúa viendo anime del historial:

`ani-cli {{[-c|--continue]}}`

- Actualiza `ani-cli`:

`ani-cli {{[-U|--update]}}`
