# pbmtonokia

> Convert a PBM image to one of Nokia's Smart Messaging Formats .
> More information: <https://netpbm.sourceforge.net/doc/pbmtonokia.html>.

- Convert a PBM image into a Nokia Operator Logo as hexcode:

`pbmtonokia -fmt NEX_NOL -net {{network_operator_code}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- Convert a PBM image into a Nokia Group Graphic as hexcode:

`pbmtonokia -fmt NEX_NGG {{path/to/image.pbm}} > {{path/to/output.hex}}`

- Convert a PBM image into a Nokia Picture Message with the specified text as hexcode:

`pbmtonokia -fmt NEX_NPM -txt {{text_message}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- Convert a PBM image into a Nokia Operator Logo as a NOL file:

`pbmtonokia -fmt NOL {{path/to/image.pbm}} > {{path/to/output.nol}}`

- Convert a PBM image into a Nokia Group Graphic as an NGG file:

`pbmtonokia -fmt NGG {{path/to/image.pbm}} > {{path/to/output.ngg}}`

- Convert a PBM image into a Nokia Picture Message as an NPM file:

`pbmtonokia -fmt NPM {{path/to/image.pbm}} > {{path/to/output.npm}}`
