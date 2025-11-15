# ppmtopjxl

> Convert a PPM image into an HP PaintJet XL PCL file.
> More information: <https://netpbm.sourceforge.net/doc/ppmtopjxl.html>.

- Convert a PPM image into an PJXL file:

`ppmtopjxl {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Resize the input image:

`ppmtopjxl {{[-xsi|-xsize]}} {{10cm}} {{[-ysi|-ysize]}} {{5cm}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Shift the input image:

`ppmtopjxl {{[-xsh|-xshift]}} {{10pt}} {{[-ysh|-yshift]}} {{5pt}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Do not use the normal TIFF 4.0 compression method:

`ppmtopjxl {{[-n|-nopack]}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`
