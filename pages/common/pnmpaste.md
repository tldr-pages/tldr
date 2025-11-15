# pnmpaste

> Paste a PNM image into another PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmpaste.html>.

- Paste a PNM image into another PNM image at the specified coordinates:

`pnmpaste {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`

- Paste the image read from `stdin` into the specified image:

`{{command}} | pnmpaste {{x}} {{y}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Combine the overlapping pixels by the specified boolean operation, where white pixels represent `true` while black pixels represent `false`:

`pnmpaste -{{and|nand|or|nor|xor|xnor}} {{x}} {{y}} {{path/to/image1.pnm}} {{path/to/image2.pnm}} > {{path/to/output.pnm}}`
