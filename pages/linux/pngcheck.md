# pngcheck

> Useful forensics tool for validating the integrity of image files.
> Can also extract embedded images and text from the file.
> More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Verify the integrity of an image file:

`pngcheck {{image}}`

- Check the file with [v]erbose and [c]olorized output:

`pngcheck -vf {{image}}`

- Display contents of [t]ext chunks and [s]earch for PNGs within the file:

`pngcheck -ts {{image}}`

- Search for and e[x]tract embedded PNGs within the file:

`pngcheck -x {{image}}`
