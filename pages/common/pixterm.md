# pixterm

> Image printing in the terminal.
> See also: `chafa` and `catimg`.
> More information: <https://github.com/eliukblau/pixterm>.

- Print a static image to the terminal:

`pixterm {{path/to/input}}`

- Use the image's original aspect ratio:

`pixterm -s 2 {{path/to/input}}`

- Specify a custom aspect ratio with [t]erminal [r]ows and [c]olumns:

`pixterm -tr {{rows}} -tc {{columns}} {{path/to/input}}`

- Filter the output with a [m]atte background color and character [d]ithering:

`pixterm -m {{000000}} -d 2 {{path/to/input}}`
