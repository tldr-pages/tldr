# carbon-now

> Create beautiful images of code.
> More information: <https://github.com/mixn/carbon-now-cli>.

- Create an image from a file using default settings:

`carbon-now {{path/to/file}}`

- Create an image from a text in clipboard using default settings:

`carbon-now --from-clipboard`

- Create an image from `stdin` using default settings and copy to the clipboard:

`{{input}} | carbon-now --to-clipboard`

- Create images interactively for custom settings and optionally save a preset:

`carbon-now {{[-i|--interactive]}} {{path/to/file}}`

- Create images from a previously saved preset:

`carbon-now {{[-p|--preset]}} {{preset}} {{path/to/file}}`

- Start at a specified line of text:

`carbon-now {{[-s|--start]}} {{line}} {{path/to/file}}`

- End at a specific line of text:

`carbon-now {{[-e|--end]}} {{line}} {{path/to/file}}`

- Open image in a browser instead of saving:

`carbon-now --open {{path/to/file}}`
