# pnmpad

> Add borders to a PNM image.
> See also: `pnmmargin`, `pamcut`, `pamcomp`.
> More information: <https://netpbm.sourceforge.net/doc/pnmpad.html>.

- Add borders of the specified sizes to the image:

`pnmpad {{[-l|-left]}} {{100}} {{[-ri|-right]}} {{150}} {{[-t|-top]}} {{123}} {{[-bo|-bottom]}} {{456}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the image to the specified size:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-he|-height]}} {{500}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the width of the image to the specified size, controlling the ratio between right and left padding:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-ha|-halign]}} {{0.7}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Pad the width of the image using the specified color:

`pnmpad {{[-wi|-width]}} {{1000}} {{[-c|-color]}} {{red}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
