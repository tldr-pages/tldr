# ppmrainbow

> Generate a rainbow.
> More information: <https://netpbm.sourceforge.net/doc/ppmrainbow.html>.

- Generate a rainbow consisting of the specified colors:

`ppmrainbow {{color1 color2 ...}} > {{path/to/output_file.ppm}}`

- Specify the size of the output in pixels:

`ppmrainbow -width {{width}} -height {{height}} {{color1 color2 ...}} > {{path/to/output_file.ppm}}`

- End the rainbow with the last color specified, do not repeat the first color:

`ppmrainbow -norepeat {{color1 color2 ...}} > {{path/to/output_file.ppm}}`
