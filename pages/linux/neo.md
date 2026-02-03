# neo

> Simulate the digital rain from "The Matrix".
> See also: `cmatrix`.
> More information: <https://manned.org/neo>.

- Run the default digital rain:

`neo`

- Set scroll speed and asynchronous columns:

`neo {{[-S|--speed]}} 12 {{[-a|--async]}}`

- Change text color and colormode:

`neo {{[-c|--color]}} green --colormode 256`

- Display a centered message:

`neo {{[-m|--message]}} "Hello World"`

- Set droplet density and glitch percentage: 

`neo -d 2.0 {{[-g|--glitchpct]}} 5.0`

- Use a specific charset (ASCII, Cyrillic, Greek, Katakana, Braille):

`neo --charset ascii`

- Disable glitching and colors for performance:

`neo --noglitch --colormode 0`

- Clear screen, (Increase / Decrease speed), (Increase / Decrease glitchiness), (Increase / Decrease droplets), Quit:

`<Space>, (<Up> / <Down>), (<Left> / <Right>), (<+> / <->), (<Esc> / <q>)`
