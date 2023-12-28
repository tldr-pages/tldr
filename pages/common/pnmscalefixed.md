# pnmscalefixed

> Scale a PNM file quickly with possibly reduced quality.
> See also: `pamscale`.
> More information: <https://netpbm.sourceforge.net/doc/pnmscalefixed.html>.

- Scale an image such that the result has the specified dimensions:

`pnmscalefixed -width {{width}} -height {{height}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Scale an image such that the result has the specified width, keeping the aspect ratio:

`pnmscalefixed -width {{width}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Scale an image such that its width and height is changed by the specified factors:

`pnmscalefixed -xscale {{x_factor}} -yscale {{y_factor}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
