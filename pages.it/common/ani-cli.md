# ani-cli

> Naviga e guarda anime online.
> Vedi anche: `animdl`.
> Maggiori informazioni: <https://manned.org/ani-cli>.

- Cerca anime per nome:

`ani-cli "{{titolo_anime}}"`

- Scarica un episodio:

`ani-cli {{[-d|--download]}} "{{titolo_anime}}"`

- Scarica un intervallo di episodi:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{titolo_anime}}"`

- Scarica l'intera serie (tutti gli episodi):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 -1}}" "{{titolo_anime}}"`

- Usa VLC come player multimediale:

`ani-cli {{[-v|--vlc]}} "{{titolo_anime}}"`

- Guarda un episodio specifico:

`ani-cli {{[-e|--episode]}} {{numero_episodio}} "{{titolo_anime}}"`

- Continua a guardare dall'ultima posizione nella cronologia:

`ani-cli {{[-c|--continue]}}`

- Aggiorna `ani-cli`:

`ani-cli {{[-U|--update]}}`
