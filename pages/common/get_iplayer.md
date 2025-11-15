# get_iplayer

> Indexing tool and personal video recorder for BBC iPlayer and BBC Sounds.
> More information: <https://github.com/get-iplayer/get_iplayer/wiki/manpage>.

- Search programmes by name:

`get_iplayer "{{program_name}}"`

- Record programme by results of search:

`get_iplayer "{{program_name}}" {{[-g|--get]}}`

- Record programme by URL from the BBC iPlayer website:

`get_iplayer "https://www.bbc.co.uk/iplayer/episode/{{program_PID}}/{{name-of-show-episode-number-episode-title}}"`

- Download subtitles for a programme by results of search:

`get_iplayer "{{program_name}}" --subtitles-only`

- Search for a programme, record it and download subtitles:

`get_iplayer "{{program_name}}" {{[-g|--get]}} --subtitles`

- Display help:

`get_iplayer {{[-h|--help]}}`
