# neo

> Simulate the digital rain from "The Matrix".
> See also: `cmatrix`.
> More information: <https://manned.org/neo>.

- Run the default digital rain:

`neo`

- Set scroll speed and asynchronous columns:

`neo {{[-S|--speed]}} 12 {{[-a|--async]}}`

- Change text color ([c]) and color mode:

`neo {{[-c|--color]}} green --colormode 256`

- Display a centered message ([m]):

`neo -m "Hello World"`

- Set droplet density ([d]) and glitch percentage ([G]):

`neo -d 2.0 --glitchpct=5.0`

- Use a specific charset (ASCII, Cyrillic, Greek, Katakana, Braille):

`neo --charset=ascii`

- Disable glitching ([noglitch]) and colors ([colormode=0]) for performance:

`neo --noglitch --colormode=0`

- Clear screen, (Increase / Decrease speed), (Increase / Decrease glitchiness), (Increase / Decrease droplets), Quit:

`<Space>, (<Up> / <Down>), (<Left> / <Right>), (<+> / <->), (<Esc> / <q>)`
