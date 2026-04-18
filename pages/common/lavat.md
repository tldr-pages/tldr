# lavat

> Display an animated lava lamp effect in the terminal.
> Customize colors, speed, size, movement, and display style.
> More information: <https://github.com/AngelJumbo/lavat>.

- Start the default lava animation:

`lavat`

- Start with named lava and rim colors:

`lavat -c {{green}} -k {{red}}`

- Start in gradient mode with two hex colors:

`lavat -g -c {{00FF00}} -k {{FF0000}}`

- Start with gravity and buoyancy movement enabled:

`lavat -G`

- Start with a custom speed, radius, rim size, and number of metaballs:

`lavat -s {{1..10}} -r {{1..10}} -R {{1..5}} -b {{5..20}}`

- Start with a custom ASCII character set:

`lavat -F "{{.oO@}}"`

- Display help:

`lavat -h`
