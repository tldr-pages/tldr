# palmtopnm

> Convert a Palm Bitmap file to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Generate the PNM image as output, for a Palm Bitmap file as input:

`palmtopnm {{path/to/file.palm}}`

- Display various information about the input Palm Bitmap file and process:

`palmtopnm -verbose {{path/to/file.palm}}`

- Generate a histogram of colours in the input Palm Bitmap file to `stderr`:

`palmtopnm -showhist {{path/to/file.palm}}`

- Display version:

`palmtopnm -version`
