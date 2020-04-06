# playerctl

> Utility to control different media players.

- Toggle play:

`playerctl play-pause`

- Next media:

`playerctl next`

- Previous media:

`playerctl previous`

- List all players:

`playerctl --list-all`

- Send a command to a specific player:

`playerctl --player={{player_name}} {{command}}`

- Send a command to all players:

`playerctl --all-players {{command}}`

- Show now playing:

`playerctl metadata --format "Now playing: {{artist}} - {{album}} - {{title}}"`
