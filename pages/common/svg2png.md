# svg2png

> Render an SVG image to a PNG image using cairo.
> More information: <http://cairographics.org/>.

- Convert an SVG file to PNG:

`svg2png {{path/to/file.svg}} {{path/to/output.png}}`

- Convert an SVG file to PNG with a specific width (preserving aspect ratio):

`svg2png {{[-w|--width]}} {{800}} {{path/to/file.svg}} {{path/to/output.png}}`

- Convert an SVG file to PNG with a specific height (preserving aspect ratio):

`svg2png {{[-h|--height]}} {{600}} {{path/to/file.svg}} {{path/to/output.png}}`

- Convert an SVG file to PNG with both width and height (image centered in space):

`svg2png {{[-w|--width]}} {{800}} {{[-h|--height]}} {{600}} {{path/to/file.svg}} {{path/to/output.png}}`

- Convert an SVG file to PNG scaled by a factor:

`svg2png {{[-s|--scale]}} {{2.0}} {{path/to/file.svg}} {{path/to/output.png}}`

- Convert an SVG from stdin to PNG on stdout:

`cat {{path/to/file.svg}} | svg2png - - > {{path/to/output.png}}`

- Flip the output image horizontally or vertically:

`svg2png --flipx {{path/to/file.svg}} {{path/to/output.png}}`
