# pamdice

> Slice a Netpbm image vertically or horizontally.
> See also: `pamundice`.
> More information: <https://netpbm.sourceforge.net/doc/pamdice.html>.

- Slice a Netpbm image such that the resulting tiles have the specified height and width:

`pamdice -outstem {{filename_stem}} -height {{value}} -width {{value}} {{path/to/input.ppm}}`

- Make the prodced pieces overlap by the specified amount horizontally and vertically:

`pamdice -outstem {{filename_stem}} -height {{value}} -width {{value}} -hoverlap {{value}} -voverlap {{value}} {{path/to/input.ppm}}`
