# mocp

> Music on Console (MOC) audio player.
> More information: <http://moc.daper.net/>.

- Launch MOC terminal UI:

`mocp`

- Launch MOC terminal UI in specific directory:

`mocp {{path/to/directory}}`

- Launch MOC in background:

`mocp &`

- Add individual song to play queue while MOC is in background:

`mocp --enqueue {{path/to/audio_file}}`

- Add songs recursively to play queue while MOC is in background:

`mocp --append {{path/to/directory}}`

- Clear the play queue while MOC is in background:

`mocp --clear`

- Play first song in play queue while MOC is in background:

`mocp --play`

- Stop any playing songs while MOC is in background:

`mocp --stop`

- Close MOC while it is in backgroud:

`mocp --exit`
