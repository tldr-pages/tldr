# pixterm

> Image printing in the terminal.
> See also: `chafa`, `catimg`.
> More information: <https://github.com/eliukblau/pixterm>.

- Render a static image directly in the terminal:

`pixterm {{path/to/file}}`

- Use the image's original aspect ratio:

`pixterm -s 2 {{path/to/file}}`

- Specify a custom aspect ratio using a specific number of [t]erminal [r]ows and [c]olumns:

`pixterm -tr {{24}} -tc {{80}} {{path/to/file}}`

- Filter the output with a [m]atte background color and character [d]ithering:

`pixterm -m {{000000}} -d 2 {{path/to/file}}`
