# optipng

> PNG image file optimization utility.

- Compress a PNG with default settings:

`optipng {{file.png}}`

- Compress a PNG as optimally (but slowly) as possible:

`optipng -o{{7}} {{file.png}}`

- Compress a PNG as quickly (but non-optimally) as possible:

`optipng -o{{0}} {{file.png}}`

- Compress a PNG and add interlacing:

`optipng -i {{1}} {{file.png}}`

- Compress a PNG and remove all metadata:

`optipng -strip all {{file.png}}`
