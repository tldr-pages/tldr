# avifenc

> AV1 Image File Format (AVIF) encoder.
> More information: <https://aomediacodec.github.io/av1-avif/>.

- Convert a specific PNG image to AVIF:

`avifenc {{path/to/input.png}} {{path/to/output.avif}}`

- Encode with a specific speed (6=default, 0=slowest and 10=fastest):

`avifenc --speed {{2}} {{path/to/input.png}} {{path/to/output.avif}}`
