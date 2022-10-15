# pngcheck

> Useful forensics tool for validating the integrity of PNG based (.png|.jng|.mng) image files.
> Can also extract embedded images and text from a file.
> More information: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Verify the integrity of an image file:

`pngcheck {{file.png}}`

- Check the file with [v]erbose and [c]olorized output:

`pngcheck -vf {{file.png}}`

- Display contents of [t]ext chunks and [s]earch for PNGs within the file:

`pngcheck -ts {{file.png}}`

- Search for, and e[x]tract embedded PNGs within the file:

`pngcheck -x {{file.png}}`
