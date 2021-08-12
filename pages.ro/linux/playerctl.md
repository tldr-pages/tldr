# playerctl

> Utilitate pentru a controla diferite playere media.
> Mai multe informaţii: <https://github.com/altdesktop/playerctl>

- Comută jocul:

`playerctl play-pause`

- Următoarea mass-media:

`playerctl next`

- Presa anterioară:

`playerctl previous`

- Lista tuturor jucătorilor:

`playerctl --list-all`

- Trimite o comandă unui anumit jucător:

`playerctl --player={{player_name}} {{command}}`

- Trimite o comandă tuturor jucătorilor:

`playerctl --all-players {{command}}`

- Arată acum joc:

`playerctl metadata --format "Now playing: {{artist}} - {{album}} - {{title}}"`
