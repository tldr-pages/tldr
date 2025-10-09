# inkscape

> An SVG (Scalable Vector Graphics) editing program.
> For Inkscape versions up to 0.92.x, use -e instead of -o.
> More information: <https://inkscape.org>.

- Open an SVG file in the Inkscape GUI:

`inkscape {{path/to/file.svg}}`

- Export an SVG file into a bitmap with the default format (PNG) and the default resolution (96 DPI):

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}}`

- Export an SVG file into a bitmap of 600x400 pixels (aspect ratio distortion may occur):

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}} {{[-w|--export-width]}} 600 {{[-h|--export-height]}} 400`

- Export the drawing (bounding box of all objects) of an SVG file into a bitmap:

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.png}} {{[-D|--export-area-drawing]}}`

- Export a single object, given its ID, into a bitmap:

`inkscape {{path/to/file.svg}} {{[-i|--export-id]}} {{id}} {{[-o|--export-filename]}} {{object.png}}`

- Export an SVG document to PDF, converting all texts to paths:

`inkscape {{path/to/file.svg}} {{[-o|--export-filename]}} {{path/to/file.pdf}} {{[-T|--export-text-to-path]}}`

- Duplicate the object with id="path123", rotate the duplicate 90 degrees, save the file, and quit Inkscape:

`inkscape {{path/to/file.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
