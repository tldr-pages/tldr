# pngquant

> PNG converter and lossy image compressor.
> More information: <https://pngquant.org/>.

- Compress PNG with color quality between 65 and 80 (skip if below min value):

`pngquant --quality={{65-80}} {{path/to/file.png}}`

- Create a new image with the number of colors reduced to 64:

`pngquant {{64}} {{path/to/file.png}}`
