# conky

> Light-weight system monitor for X.

- Launch with default, built-in config:

`conky`

- Create a new, default config:

`conky -C > ~/.conkyrc`

- Load a config file:

`conky -c {{/path/to/config}}`

- Start in the background (daemonize):

`conky -d`

- Align specified config file on screen:

`conky -c {{path/to/config}} -a {{{top,bottom,middle}_{left,right,middle}}}`

- Wait 5 seconds and launch the conky config in a specified path:

`conky -p 5 -c {{path/to/config}}`
