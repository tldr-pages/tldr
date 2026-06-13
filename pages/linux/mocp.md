# mocp

> Music on Console (MOC) audio player.
> More information: <https://manned.org/mocp>.

- Launch the MOC terminal UI:

`mocp`

- Launch the MOC terminal UI in a specific directory:

`mocp {{path/to/directory}}`

- Start the MOC server in the background, without launching the MOC terminal UI:

`mocp {{[-S|--server]}}`

- Add a specific song to the play queue while MOC is in the background:

`mocp {{[-q|--enqueue]}} {{path/to/audio_file}}`

- Add songs recursively to the play queue while MOC is in the background:

`mocp {{[-a|--append]}} {{path/to/directory}}`

- Clear the play queue while MOC is in the background:

`mocp {{[-c|--clear]}}`

- Play or stop the currently queued song while MOC is in the background:

`mocp --{{play|stop}}`

- Stop the MOC server while it's in the background:

`mocp {{[-x|--exit]}}`
