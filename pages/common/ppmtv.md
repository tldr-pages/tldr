# ppmtv

> Make a PPM Image look like taken from an American TV.
> Dim every other row of image data down by the specified dim factor (a number between 0 and 1).
> More information: <https://netpbm.sourceforge.net/doc/ppmtv.html>.

- Give the PPM image an American TV appearance:

`ppmtv {{dim_factor}} {{path/to/file.ppm}} > {{path/to/output.ppm}}`

- Suppress all informational messages:

`ppmtv -quiet`

- Display version:

`ppmtv -version`
