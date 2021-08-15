# optipng

> PNG file optimization utility.
> More information: <http://optipng.sourceforge.net>.

- Compress a PNG with default settings:

`optipng {{path/to/file.png}}`

- Compress a PNG with the best compression:

`optipng -o{{7}} {{path/to/file.png}}`

- Compress a PNG with the fastest compression:

`optipng -o{{0}} {{path/to/file.png}}`

- Compress a PNG and add interlacing:

`optipng -i {{1}} {{path/to/file.png}}`

- Compress a PNG and preserve all metadata (including file timestamps):

`optipng -preserve {{path/to/file.png}}`

- Compress a PNG and remove all metadata:

`optipng -strip all {{path/to/file.png}}`
