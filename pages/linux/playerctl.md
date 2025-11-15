# playerctl

> Control media players via MPRIS.
> More information: <https://github.com/altdesktop/playerctl>.

- Toggle play:

`playerctl play-pause`

- Skip to the next track:

`playerctl next`

- Go back to the previous track:

`playerctl previous`

- List all players:

`playerctl {{[-l|--list-all]}}`

- Send a command to a specific player:

`playerctl {{[-p|--player]}} {{player_name}} {{play-pause|next|previous|...}}`

- Send a command to all players:

`playerctl {{[-a|--all-players]}} {{play-pause|next|previous|...}}`

- Display metadata about the current track:

`playerctl metadata {{[-f|--format]}} "{{Now playing: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
