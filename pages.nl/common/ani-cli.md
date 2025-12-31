# ani-cli

> Blader door anime en bekijk ze.
> Zie ook: `animdl`.
> Meer informatie: <https://manned.org/ani-cli>.

- Zoek naar anime op naam:

`ani-cli "{{anime_titel}}"`

- Download een aflevering:

`ani-cli {{[-d|--download]}} "{{anime_titel}}"`

- Download een reeks van afleveringen:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{anime_title}}"`

- Download de gehele serie (een reeks van alle afleveringen):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{anime_titel}}"`

- Gebruik VLC als de media player:

`ani-cli {{[-v|--vlc]}} "{{anime_titel}}"`

- Bekjk een specifieke aflevering:

`ani-cli {{[-e|--episode]}} {{afleveringnummer}} "{{anime_titel}}"`

- Bekijk anime verder uit je geschiedenis:

`ani-cli {{[-c|--continue]}}`

- Update `ani-cli`:

`ani-cli {{[-U|--update]}}`
