# nhentai

> Download doujinshis from nhentai.
> More information: <https://github.com/RicterZ/nhentai#usage>.

- Set cookies:

`nhentai --cookie "csrftoken={{TOKEN}}; sessionid={{ID}}"`

- Download a specific doujin:

`nhentai --id {{number}}`

- Download the first page of your favorites:

`nhentai {{[-F|--favorites]}} {{[-D|--download]}} {{[-d|--delay]}} 1`

- Download specific pages of your favorites:

`nhentai {{[-F|--favorites]}} --pages {{start_page}}-{{end_page}} {{[-D|--download]}} {{[-d|--delay]}} 1`
