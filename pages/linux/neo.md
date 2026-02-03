# neo

> Simulate the digital rain from "The Matrix".
> See also: `cmatrix`.
> More information: <https://manned.org/neo>.

- Set scroll speed and asynchronous columns:

`neo {{[-S|--speed]}} 12 {{[-a|--async]}}`

- Change text color and colormode:

`neo {{[-c|--color]}} green --colormode 256`

- Display a centered message:

`neo {{[-m|--message]}} "Hello World"`

- Set droplet density and glitch percentage:

`neo {{[-d|--density]}} 2.0 {{[-g|--glitchpct]}} 20.0`

- Use a specific charset (ascii, greek, cyrillic, arabic, braille, runic, etc.):

`neo --charset ascii`

- Clear the screen:

`<Space>`

- Show the help message:

`neo {{[-h|--help]}}`

- Exit neo:

`<Esc>|<q>`