# ani-cli

> Een cli om door anime te bladeren en deze te bekijken.
> Meer informatie: <https://manned.org/ani-cli>.

- Zoek naar anime op naam:

`ani-cli "{{anime_naam}}"`

- Download een aflevering:

`ani-cli {{[-d|--download]}} "{{anime_naam}}"`

- Download een reeks van afleveringen:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{anime_naam}}"`

- Download de gehele serie (een reeks van alle afleveringen):

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{anime_naam}}"`

- Gebruik VLC als de media player:

`ani-cli {{[-v|-vlc]}} "{{anime_naam}}"`

- Bekjk een specifieke aflevering:

`ani-cli {{[-e|--episode]}} {{afleveringnummer}} "{{anime_naam}}"`

- Bekijk anime verder uit je geschiedenis:

`ani-cli {{[-c|--continue]}}`

- Update `ani-cli`:

`ani-cli {{[-U|--update]}}`
