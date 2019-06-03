# guetzli

> JPEG image compression utility.
> More information: <https://github.com/google/guetzli>.

- Compress a JPEG image:

`guetzli {{input.jpg}} {{output.jpg}}`

- Create compressed JPEG image from PNG image:

`guetzli {{input.png}} {{output.jpg}}`

- Compress a JPEG image with desired visual quality (84-100):

`guetzli --quality {{quality_value}} {{input.jpg}} {{output.jpg}}`
