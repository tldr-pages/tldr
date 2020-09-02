# carbon-now

> Create beautiful images of code.
> More at <https://github.com/mixn/carbon-now-cli> and <https://carbon.now.sh>.

- Create image from file using default settings:

`carbon-now {{file}}`

- Create image from text in clipboard using default settings:

`carbon-now --from-clipboard`

- Create image standard input using default settings:

`{{text input}} | carbon-now`

- Create images interactively for custom settings and optionaly save a preset:

`carbon-now -i {{file}}`

- Create images from previosly saved preset:

`carbon-now -p {{preset}} {{file}}`

- Start at a specified line of text:

`carbon-now -s {{line}} {{file}}`

- End at a specific line of text:

`carbon-now -e {{line}} {{file}}`

- Open image in browser instead of saving:

`carbon-now --open {{file}}`
