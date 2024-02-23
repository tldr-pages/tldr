# pammixinterlace

> Merge each row in an image with its two neighbours.
> See also: `pamdeinterlace`.
> More information: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>.

- Merge each row in an image with its two neighbours:

`pammixinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Use the specified filtering mechanism:

`pammixinterlace -filter {{linear|fir|ffmpeg}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Turn on adaptive filtering mode, i.e., only modify pixels that are obviously part of a comb pattern:

`pammixinterlace -adaptive {{path/to/image.ppm}} > {{path/to/output.ppm}}`
