# neo

> Simulate the digital rain from "The Matrix".
> See also: `cmatrix`.
> More information: <https://manned.org/neo>.

- Set scroll speed and asynchronous columns:

`neo {{[-S|--speed]}} {{12}} {{[-a|--async]}}`

- Change text color and colormode:

`neo {{[-c|--color]}} {{green}} --colormode {{256}}`

- Display a centered message:

`neo {{[-m|--message]}} "{{Hello World}}"`

- Set droplet density and glitch percentage:

`neo {{[-d|--density]}} {{2.0}} {{[-G|--glitchpct]}} {{20.0}}`

- Use a specific charset:

`neo --charset {{ascii|greek|cyrillic|arabic|braille|runic|...}}`

- Clear the screen:

`<Space>`

- Exit neo:

`{{<Esc>|<q>}}`

- Display help:

`neo {{[-h|--help]}}`
