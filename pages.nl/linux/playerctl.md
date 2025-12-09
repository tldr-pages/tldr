# playerctl

> Bestuur mediaspelers via MPRIS.
> Meer informatie: <https://github.com/altdesktop/playerctl#using-the-cli>.

- Start/stop met afspelen:

`playerctl play-pause`

- Ga naar het volgende nummer:

`playerctl next`

- Ga terug naar het vorige nummer:

`playerctl previous`

- Toon alle spelers:

`playerctl {{[-l|--list-all]}}`

- Stuur een commando naar een specifieke speler:

`playerctl {{[-p|--player]}} {{spelernaam}} {{play-pause|next|previous|...}}`

- Stuur een commando naar alle spelers:

`playerctl {{[-a|--all-players]}} {{play-pause|next|previous|...}}`

- Toon metadata over het huidige nummer:

`playerctl metadata {{[-f|--format]}} "{{Huidig nummer: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
