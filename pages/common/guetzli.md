# guetzli

> JPEG image compression utility.
> More information: <https://manned.org/guetzli>.

- Compress a JPEG image:

`guetzli {{input.jpg}} {{output.jpg}}`

- Create a compressed JPEG from a PNG:

`guetzli {{input.png}} {{output.jpg}}`

- Compress a JPEG with the desired visual quality (84-100):

`guetzli --quality {{quality_value}} {{input.jpg}} {{output.jpg}}`
