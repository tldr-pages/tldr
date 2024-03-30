# ppmpat

> Produce a PPM image with a pattern.
> More information: <https://netpbm.sourceforge.net/doc/ppmpat.html>.

- Produce a PPM file of the specified pattern with the specified dimensions:

`ppmpat -{{gingham2|gingham3|madras|tartan|poles|...}} {{width}} {{height}} > {{path/to/file.ppm}}`

- Produce a PPM file of a camo pattern using the specified colors:

`ppmpat -camo -color {{color1,color2,...}} {{width}} {{height}} > {{path/to/file.ppm}}`
