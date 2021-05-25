# carbon-now

> Create beautiful images of code.
> More information: <https://github.com/mixn/carbon-now-cli>.

- Create an image from a file using default settings:

`carbon-now {{file}}`

- Create an image from a text in clipboard using default settings:

`carbon-now --from-clipboard`

- Create an image from standard input using default settings:

`{{input}} | carbon-now`

- Create images interactively for custom settings and optionally save a preset:

`carbon-now -i {{file}}`

- Create images from previously saved preset:

`carbon-now -p {{preset}} {{file}}`

- Start at a specified line of text:

`carbon-now -s {{line}} {{file}}`

- End at a specific line of text:

`carbon-now -e {{line}} {{file}}`

- Open image in a browser instead of saving:

`carbon-now --open {{file}}`
