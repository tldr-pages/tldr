# get_iplayer

> Indexing tool and personal video recorder for BBC iPlayer and BBC Sounds.
> More information: <https://github.com/get-iplayer/get_iplayer/wiki/manpage>.

- Search programs by name:

`get_iplayer "{{program_name}}"`

- Record program by results of search:

`get_iplayer "{{program_name}}" {{[-g|--get]}}`

- Record program by URL from the BBC iPlayer website:

`get_iplayer "https://www.bbc.co.uk/iplayer/episode/{{program_PID}}/{{name-of-show-episode-number-episode-title}}"`

- Download subtitles for a program by results of search:

`get_iplayer "{{program_name}}" --subtitles-only`

- Search for a program, record it and download subtitles:

`get_iplayer "{{program_name}}" {{[-g|--get]}} --subtitles`

- Display help:

`get_iplayer {{[-h|--help]}}`
