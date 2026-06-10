# ppmtoxpm

> Փոխարկեք PPM պատկերը X11 տարբերակի 3-րդ պիքսքարտի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtoxpm.html>:.

- Փոխակերպեք PPM պատկերը XPM պատկերի.:

`ppmtoxpm {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- Նշեք նախածանցի տողը ելքային XPM պատկերում.:

`ppmtoxpm {{[-n|-name]}} {{prefix_string}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- Ելքային XPM ֆայլում նշեք գույները իրենց տասնվեցական կոդով` իրենց անվան փոխարեն.:

`ppmtoxpm {{[-h|-hexonly]}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- Օգտագործեք նշված PGM ֆայլը որպես թափանցիկության դիմակ.:

`ppmtoxpm {{[-a|-alphamask]}} {{path/to/alpha_file.pgm}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`
