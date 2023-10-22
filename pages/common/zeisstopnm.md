# zeisstopnm

> Convert a Zeiss confocal file to Netbpm format.
> More information: <https://manned.org/zeisstopnm.1>.

- Convert a Zeiss cofocal file into either `.pgm` or `.ppm` format:

`zeisstopnm {{path/to/file}}`

- Convert a Zeiss cofocal file to Netbpm format while explicitly specifying the target file type:

`zeisstopnm -{{pgm|ppm}} {{path/to/file}}`
