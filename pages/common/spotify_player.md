# spotify_player

> A TUI Spotify client that implements all features of the official Spotify app.
> More information: <https://github.com/aome510/spotify-player#commands>.

- Start a daemon that plays music in the background:

`spotify_player {{[-d|--daemon]}}`

- Start the TUI (controls the daemon if available, otherwise starts its own client):

`spotify_player`

- Use the specified theme:

`spotify_player {{[-t|--theme]}} {{theme_name}}`

- Use configuration files (`app.toml`, `keymap.toml` and `theme.toml`) in the specified directory:

`spotify_player {{[-c|--config-folder]}} {{path/to/directory}}`

- Like the currently playing track:

`spotify_player like`

- Display a list of keybindings:

`<?>`
