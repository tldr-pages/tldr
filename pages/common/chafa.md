# chafa

> Image printing in the terminal.
> See also: `catimg` and `pixterm`.
> More information: <https://hpjansson.org/chafa>.

- Print an image or animated GIF to the terminal:

`chafa {{path/to/input}}`

- Use 24-bit [c]olor:

`chafa -c full {{path/to/input}}`

- Use dithering to improve output with small color palettes:

`chafa -c 16 --dither ordered {{path/to/input}}`

- Generate output like a low-resolution raster image:

`chafa --symbols vhalf {{path/to/input}}`

- Generate monochrome output with only Braille characters:

`chafa -c none --symbols braille {{path/to/input}}`
