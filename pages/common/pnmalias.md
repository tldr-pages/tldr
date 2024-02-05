# pnmalias

> Apply antialiasing onto a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmalias.html>.

- Perform antialiasing on a PNM image, taking black pixels as background and white pixels as foreground:

`pnmalias {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Explicitly specify the background and foreground color:

`pnmalias -bcolor {{background_color}} -fcolor {{foreground_color}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Apply altialiasing to foreground pixels only:

`pnmalias -fonly {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Apply antialiasing to all surrounding pixels of background pixels:

`pnmalias -balias {{path/to/input.pnm}} > {{path/to/output.ppm}}`
