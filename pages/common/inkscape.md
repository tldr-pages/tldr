# inkscape

> An SVG (Scalable Vector Graphics) editing program.
> Use -z to not open the GUI and only process files in the console.
> More information: <https://inkscape.org>.

- Open an SVG file in the Inkscape GUI:

`inkscape {{filename.svg}}`

- Export an SVG file into a bitmap with the default format (PNG) and the default resolution (90 DPI):

`inkscape {{filename.svg}} -e {{filename.png}}`

- Export an SVG file into a bitmap of 600x400 pixels (aspect ratio distortion may occur):

`inkscape {{filename.svg}} -e {{filename.png}} -w {{600}} -h {{400}}`

- Export a single object, given its ID, into a bitmap:

`inkscape {{filename.svg}} -i {{id}} -e {{object.png}}`

- Export an SVG document to PDF, converting all texts to paths:

`inkscape {{filename.svg}} --export-pdf={{filename.pdf}} --export-text-to-path`

- Duplicate the object with id="path123", rotate the duplicate 90 degrees, save the file, and quit Inkscape:

`inkscape {{filename.svg}} --select=path123 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileQuit`
