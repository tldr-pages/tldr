# pngcheck

> Forensics tool for validating the integrity of PNG based (PNG, JNG, MNG) image files.
> Can also extract embedded images and text from a file.
> More information: <https://github.com/pnggroup/pngcheck>.

- Verify the integrity of an image file (width, height, and color depth):

`pngcheck {{path/to/image.png}}`

- Print information for an image with [c]olorized output:

`pngcheck -c {{path/to/image.png}}`

- Print [v]erbose information for an image:

`pngcheck -cvt {{path/to/image.png}}`

- Receive an image from `stdin` and display detailed information:

`cat {{path/to/image.png}} | pngcheck -cvt`

- [s]earch for PNGs within a specific file and display information about them:

`pngcheck -s {{path/to/image.png}}`

- Search for PNGs within another file and e[x]tract them:

`pngcheck -x {{path/to/image.png}}`
