# ppmcie

> Draw a CIE color chart as a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ppmcie.html>.

- Draw a CIE color chart using the REC709 color system as a PPM image:

`ppmcie > {{path/to/output.ppm}}`

- Specify the color system to be used:

`ppmcie -{{cie|ebu|hdtv|ntsc|smpte}} > {{path/to/output.ppm}}`

- Specify the location of the individual illuminants:

`ppmcie -{{red|green|blue}} {{xpos ypos}} > {{path/to/output.ppm}}`

- Do not dim the area outside the Maxwell triangle:

`ppmcie -full > {{path/to/output.ppm}}`
