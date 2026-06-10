# ppmtopjxl

> Փոխակերպեք PPM պատկերը HP PaintJet XL PCL ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtopjxl.html>:.

- Փոխակերպեք PPM պատկերը PJXL ֆայլի.:

`ppmtopjxl {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Չափափոխել մուտքագրված պատկերը.:

`ppmtopjxl {{[-xsi|-xsize]}} {{10cm}} {{[-ysi|-ysize]}} {{5cm}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Տեղափոխեք մուտքագրված պատկերը.:

`ppmtopjxl {{[-xsh|-xshift]}} {{10pt}} {{[-ysh|-yshift]}} {{5pt}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`

- Մի օգտագործեք սովորական TIFF 4.0 սեղմման մեթոդը.:

`ppmtopjxl {{[-n|-nopack]}} {{path/to/image.ppm}} > {{path/to/output.pjxl}}`
