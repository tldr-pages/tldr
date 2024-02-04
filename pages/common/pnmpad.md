# pnmpad

> Add borders to a PNM image.
> See also: `pnmmargin`, `pamcut`, `pamcomp`.
> More information: <https://netpbm.sourceforge.net/doc/pnmpad.html>.

- Add borders of the specified sizes to the image:

`pnmpad -left {{100}} -right {{150}} -top {{123}} -bottom {{456}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the image to the specified size:

`pnmpad -width {{1000}} -height {{500}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the width of the image to the specified size, controlling the ratio between right and left padding:

`pnmpad -width {{1000}} -halign {{0.7}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the width of the image using the specified color:

`pnmpad -width {{1000}} -color {{red}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
