# conky

> Light-weight system monitor for X.
> More information: <https://github.com/brndnmtthws/conky>.

- Launch with default, built-in config:

`conky`

- Create a new default config:

`conky {{[-C|--print-config]}} > ~/.conkyrc`

- Launch Conky with a given configuration file:

`conky {{[-c|--config]}} {{path/to/config}}`

- Start in the background (daemonize):

`conky {{[-d|--daemonize]}}`

- Align Conky on the desktop:

`conky {{[-a|--alignment]}} {{top|bottom|middle}}_{{left|right|middle}}`

- Pause for 5 seconds at startup before launching:

`conky {{[-p|--pause]}} {{5}}`
