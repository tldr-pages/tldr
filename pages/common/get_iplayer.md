# get_iplayer

> Indexing tool and personal video recorder for BBC iPlayer and BBC Sounds.
> More information: <https://github.com/get-iplayer/get_iplayer?tab=readme-ov-file>.

- Search programmes by name:

`get_iplayer "Name of the Program"`

- Record programme by results of search:

`get_iplayer "Name of the Program" --get`

- Record programme by URL from the BBC iPlayer website:

`get_iplayer "https://www.bbc.co.uk/iplayer/episode/PIDoftheprogram/name-of-show-episode-number-episode-title"`

- Download subtitles for a programme by results of search:

`get_iplayer "{{program_name}}" --subtitles-only`

- Search for a programme, record it and download subtitles:

`get_iplayer "{{program_name}}" {{[-g|--get]}} --subtitles`

- Display basic help page:

`get_iplayer --helpbasic`
