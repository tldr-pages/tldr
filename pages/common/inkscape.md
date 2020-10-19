# inkscape

> An SVG (Scalable Vector Graphics) editing program.
> For Inkscape versions up to 0.92.x, use -e instead of -o.
> More information: <https://inkscape.org>.

- Open an SVG file in the Inkscape GUI:

`inkscape {{filename.svg}}`

- Export an SVG file into a bitmap with the default format (PNG) and the default resolution (96 DPI):

`inkscape {{filename.svg}} -o {{filename.png}}`

- Export an SVG file into a bitmap of 600x400 pixels (aspect ratio distortion may occur):

`inkscape {{filename.svg}} -o {{filename.png}} -w {{600}} -h {{400}}`

- Export the drawing (bounding box of all objects) of an SVG file into a bitmap:

`inkscape {{filename.svg}} -o {{filename.png}} -D`

- Export a single object, given its ID, into a bitmap:

`inkscape {{filename.svg}} -i {{id}} -o {{object.png}}`

- Export an SVG document to PDF, converting all texts to paths:

`inkscape {{filename.svg}} -o {{filename.pdf}} --export-text-to-path`

- Duplicate the object with id="path123", rotate the duplicate 90 degrees, save the file, and quit Inkscape:

`inkscape {{filename.svg}} --select=path123 --verb="{{EditDuplicate;ObjectRotate90;FileSave;FileQuit}}"`
